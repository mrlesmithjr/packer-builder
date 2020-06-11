"""Generates the Packer build template."""
import os
import json
import logging
import subprocess
from subprocess import PIPE
import sys
from packer_builder.specs.builders.common import common_builder
from packer_builder.specs.builders.distro import distro_builder
from packer_builder.specs.builders.qemu import qemu_builder
from packer_builder.specs.builders.virtualbox import virtualbox_builder
from packer_builder.specs.builders.vmware import vmware_builder
from packer_builder.specs.provisioners.freenas import freenas_provisioners
from packer_builder.specs.provisioners.linux import linux_provisioners
from packer_builder.specs.provisioners.windows import windows_provisioners

# pylint: disable=too-many-arguments
# pylint: disable=too-many-instance-attributes


class Template():
    """Main Packer template execution."""

    def __init__(self, **kwargs):

        # Setup logger
        self.logger = logging.getLogger(__name__)
        # Obtain script dir from absolute path of this module
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # Setup vars for class usage
        self.build_dir = kwargs['data']['output_dir']
        self.build_scripts_dir = os.path.join(self.script_dir, 'scripts')
        self.distro = kwargs['data']['distro'].lower()
        self.distro_spec = kwargs['data']['distro_spec']
        self.http_dir = os.path.join(self.build_dir, 'http')
        self.password_override = kwargs['data']['password_override']
        self.version = kwargs['data']['version']
        self.version_spec = kwargs['data']['version_spec']

        # Define template dictionary
        self.template = dict()

        # Check if Vagrant box is to be built or not
        self.vagrant_box = self.distro_spec.get('vagrant_box')
        if self.vagrant_box is None:
            self.vagrant_box = False

    def get_vars(self):
        """Define user specific variables."""
        self.template['variables'] = {
            'compression_level': '6',
            'cpus': str(self.distro_spec['cpus']),
            'memory': str(self.distro_spec['memory']),
            'disk_adapter_type': self.distro_spec['disk_adapter_type'],
            'disk_size': str(self.distro_spec['disk_size']),
            'iso_checksum': self.version_spec['iso_checksum'],
            'iso_url': self.version_spec['iso_url'],
            'username': self.distro_spec['username'],
            'password': self.distro_spec['password'],
            'vm_name': f'{self.distro}-{self.version}',  # noqa: E999
        }
        if self.password_override is not None:
            self.template['variables']['password'] = self.password_override

    def get_builders(self):
        """Direct builder configurations based on builder type."""
        self.template['builders'] = []
        for builder_ in self.distro_spec['builders']:
            # Define build spec dictionary
            builder_spec = dict()
            # Get builder as lowercase
            builder = builder_.lower()

            # Define data to pass as kwargs
            data = {'build_dir': self.build_dir, 'http_dir': self.http_dir,
                    'distro_spec': self.distro_spec, 'distro': self.distro,
                    'script_dir': self.script_dir, 'builder': builder,
                    'builder_spec': builder_spec, 'version': self.version,
                    'vagrant_box': self.vagrant_box}

            # Define common builder specs
            builder_spec = common_builder(data=data)

            # Define distro builder specs
            distro_builder(data=data)

            # Define builder map to define function
            builder_map = {'qemu': qemu_builder,
                           'virtualbox-iso': virtualbox_builder,
                           'vmware-iso': vmware_builder}

            builder_mapping = builder_map[builder]
            builder_spec = builder_mapping(data=data)

            self.template['builders'].append(builder_spec)

    def get_provisioners(self):
        """Direct provisioners based on distro type."""

        self.template['provisioners'] = []

        # Define data to pass as kwargs
        data = {'build_scripts_dir': self.build_scripts_dir,
                'template': self.template,
                'vagrant_box': self.vagrant_box}

        if self.distro == 'freenas':
            self.template = freenas_provisioners(data=data)
        elif self.distro == 'windows':
            self.template = windows_provisioners(data=data)
        else:
            self.template = linux_provisioners(data=data)

    def get_post_processors(self):
        """Post processors for builds."""

# pylint: disable=line-too-long
        vmx_file = f'{self.build_dir}''/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}.vmx'  # noqa: E501
        ovf_file = f'{self.build_dir}''/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}.ovf'  # noqa: E501

        # Get list of builder types to properly add post processors
        builder_types = list()
        for build_type in self.template['builders']:
            builder_types.append(build_type['type'])

        # Build post processors based on builder_types
        post_processors = list()
        if 'vmware-iso' in builder_types:
            post_processors.append({
                'type': 'shell-local',
                'inline': f'ovftool {vmx_file} {ovf_file}',
                'only': ['vmware-iso']
            })
        if self.vagrant_box:
            vagrant_post_proc = {
                'compression_level': '{{ user `compression_level` }}',
                'keep_input_artifact': True,
                'output': '{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}.box',  # noqa: E501
                'type': 'vagrant'
            }
            if self.distro == 'freenas':
                vagrant_post_proc.update(
                    {'only': ['virtualbox-iso', 'vmware-iso']})
            # self.template['post-processors'].insert(1, vagrant_post_proc)
            post_processors.append(vagrant_post_proc)
        post_processors.append({
            'type': 'manifest',
            'strip_path': True
        })
        self.template['post-processors'] = post_processors

    def save(self):
        """Save generated template for building."""

        self.get_vars()
        self.get_builders()
        self.get_provisioners()
        self.get_post_processors()

        template_json = json.dumps(self.template, indent=4)
        template_file = os.path.join(self.build_dir, 'template.json')

        # If template file exists, remove it
        if os.path.isfile(template_file):
            os.remove(template_file)

        # Write new template file
        with open(template_file, 'w') as packer_template:
            packer_template.write(template_json)
            packer_template.close()

    def validate(self):
        """Validate generated Packer template."""

        current_dir = os.getcwd()
        os.chdir(self.build_dir)

        validate = subprocess.run(
            ['packer', 'validate', 'template.json'], check=False,
            stderr=PIPE, stdout=PIPE)

        # Display output back to stdout for visibility
        print(validate.stdout.decode("utf-8"))

        # Log and exit if failed
        if validate.returncode != 0:
            self.logger.error(validate)
            sys.exit(1)

        os.chdir(current_dir)
