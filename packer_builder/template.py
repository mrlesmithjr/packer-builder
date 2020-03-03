"""Generates the Packer build template."""
import os
import json
from packer_builder.specs.builders.common import common_builder
from packer_builder.specs.builders.distro import distro_builder
from packer_builder.specs.builders.qemu import qemu_builder
from packer_builder.specs.builders.virtualbox import virtualbox_builder
from packer_builder.specs.builders.vmware import vmware_builder
from packer_builder.specs.builders.vsphere import vsphere_builder
from packer_builder.specs.provisioners.freenas import freenas_provisioners
from packer_builder.specs.provisioners.linux import linux_provisioners
from packer_builder.specs.provisioners.windows import windows_provisioners

# pylint: disable=too-many-arguments
# pylint: disable=too-many-instance-attributes


class Template():
    """Main Packer template execution."""

    def __init__(self, output_dir, password_override,
                 distro, distro_spec, version, version_spec):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.build_dir = output_dir
        self.build_scripts_dir = os.path.join(self.script_dir, 'scripts')
        self.distro = distro.lower()
        self.distro_spec = distro_spec
        self.http_dir = os.path.join(self.build_dir, 'http')
        self.password_override = password_override
        self.template = dict()
        self.vagrant_box = distro_spec.get('vagrant_box')
        if self.vagrant_box is None:
            self.vagrant_box = False
        self.version = version
        self.version_spec = version_spec
        self.get_vars()
        self.get_builders()
        self.get_provisioners()
        self.get_post_processors()
        self.save_template()

    def get_vars(self):
        """Define user specific variables."""
        self.template['variables'] = {
            'compression_level': '6',
            'cpus': str(self.distro_spec['cpus']),
            'memory': str(self.distro_spec['memory']),
            'disk_adapter_type': self.distro_spec['disk_adapter_type'],
            'disk_size': str(self.distro_spec['disk_size']),
            'iso_checksum': self.version_spec['iso_checksum'],
            'iso_checksum_type': self.version_spec['iso_checksum_type'],
            'iso_url': self.version_spec['iso_url'],
            'username': self.distro_spec['username'],
            'password': self.distro_spec['password'],
            'vcenter_server': self.distro_spec['vcenter_server'],
            'vcenter_user': self.distro_spec['vcenter_user'],
            'vcenter_pass': self.distro_spec['vcenter_pass'],
            'vcenter_resource_pool': self.distro_spec['vcenter_resource_pool'],
            'vcenter_cluster': self.distro_spec['vcenter_cluster'],
            'vcenter_host': self.distro_spec['vcenter_host'],
            'vcenter_datastore': self.distro_spec['vcenter_datastore'],
            'vcenter_network': self.distro_spec['vcenter_network'],
            'vcenter_convert_to_template': self.distro_spec[
                'vcenter_convert_to_template'],
            'vm_name': f'{self.distro}-{self.version}',  # noqa: E999
        }
        if self.password_override is not None:
            self.template['variables']['password'] = self.password_override

    def get_builders(self):
        """Direct builder configurations based on builder type."""
        self.template['builders'] = []
        for builder in self.distro_spec['builders']:
            self.builder = builder.lower()
            self.builder_spec = dict()
            common_builder(self)
            distro_builder(self)
            if self.builder == 'qemu':
                qemu_builder(self)
            elif self.builder == 'virtualbox-iso':
                virtualbox_builder(self)
            elif self.builder == 'vmware-iso':
                vmware_builder(self)
            elif self.builder == "vsphere-iso":
                vsphere_builder(self)

            self.template['builders'].append(self.builder_spec)

    def get_provisioners(self):
        """Direct provisioners based on distro type."""
        self.template['provisioners'] = []
        if self.distro == 'freenas':
            freenas_provisioners(self)
        elif self.distro == 'windows':
            windows_provisioners(self)
        else:
            linux_provisioners(self)

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
            else:
                vagrant_post_proc.update(
                    {'except': ['vsphere-iso']})
            # self.template['post-processors'].insert(1, vagrant_post_proc)
            post_processors.append(vagrant_post_proc)
        post_processors.append({
            'type': 'manifest',
            'strip_path': True
        })
        self.template['post-processors'] = post_processors

    def save_template(self):
        """Save generated template for building."""
        template_json = json.dumps(self.template, indent=4)
        template_file = os.path.join(self.build_dir, 'template.json')
        if os.path.isfile(template_file):
            os.remove(template_file)
        with open(template_file, 'w') as packer_template:
            packer_template.write(template_json)
            packer_template.close()
