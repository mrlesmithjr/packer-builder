"""Build generated Packer template."""
import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime
from shutil import which
from packer_builder.template import Template


# pylint: disable=too-many-instance-attributes
class Build():
    """Main builder process."""

    def __init__(self, args, distros):
        # Setup logger
        self.logger = logging.getLogger(__name__)
        # Define distros
        self.distros = distros
        # Define build directory
        self.build_dir = args.outputdir
        # Log build directory
        self.logger.info('Build dir: %s', self.build_dir)
        # Define build manifest file
        self.build_manifest_file = os.path.join(
            self.build_dir, 'packer-builder.json')
        # Define number of days since last build
        self.num_days = args.numdays

        # Only build a single distro if passed
        if args.distro is not None:
            self.distro = args.distro
        # Build all distros
        else:
            self.distro = 'all'

        # Only build for a single builder
        if args.builder is not None:
            self.builder = args.builder
        # Build all builders
        else:
            self.builder = 'all'

        # Define password override if passed
        self.password_override = args.password
        self.load_build_manifest()
        self.iterate()

    def load_build_manifest(self):
        """Load up existing build manifest, otherwise create one."""
        if os.path.isfile(self.build_manifest_file):
            with open(self.build_manifest_file, 'r') as stream:
                self.logger.info(
                    'Loading build manifest: %s', self.build_manifest_file)
                self.build_manifest = json.load(stream)
        else:
            self.build_manifest = dict()

# pylint: disable=too-many-locals
    def iterate(self):
        """Iterate through defined distros and build them."""

        # Define current directory
        self.current_dir = os.getcwd()
        # Log current directory
        self.logger.info('Current directory: %s', self.current_dir)

        # Iterate through distros
        for distro, distro_spec in self.distros.items():
            # Log distro
            self.logger.info('distro: %s', distro)
            # Log distro spec
            self.logger.info('distro_spec: %s', distro_spec)
            # Get builders
            self.builders = distro_spec['builders']

            # Check build manifest for distro
            distro_check = self.build_manifest.get(distro)
            # Log distro check
            self.logger.info('Distro check: %s', distro_check)

            if distro_check is None:
                self.build_manifest[distro] = dict()

            if self.distro == 'all' or (self.distro != 'all' and
                                        self.distro == distro):
                for version, version_spec in distro_spec['versions'].items():
                    version = str(version)
                    version_check = self.build_manifest[distro].get(version)
                    # Log version
                    self.logger.info('version: %s', version)
                    # Log version_check
                    self.logger.info('version_check: %s', version_check)

                    if version_check is None:
                        self.build_manifest[distro][version] = {
                            'builds': []}

                    build_image = False
                    current_time_epoch = time.mktime(
                        datetime.now().timetuple())
                    last_build_time_epoch = self.build_manifest[distro][
                        version].get('last_build_time')
                    if last_build_time_epoch is not None:
                        older_than_days_epoch = current_time_epoch - \
                            (86400 * self.num_days)
                        older_than_days = int(
                            (older_than_days_epoch/86400) + 25569)
                        last_build_time = int(
                            (float(last_build_time_epoch)/86400) + 25569)
                        if last_build_time < older_than_days:
                            build_image = True
                    else:
                        build_image = True

                    self.logger.info('Build image: %s', build_image)

                    if build_image:
                        # Define data to pass to class
                        data = {'output_dir': self.build_dir,
                                'password_override': self.password_override,
                                'distro': distro, 'distro_spec': distro_spec,
                                'version': version,
                                'version_spec': version_spec}

                        # Generate the template
                        template = Template(data=data)
                        # Save template for processing
                        template.save()

                        # # Validate template
                        # self.validate()
                        template.validate()

                        # Build image from template
                        self.build()

                        self.build_manifest[distro][version][
                            'last_build_time'] = current_time_epoch

                        build_info = {
                            'builder_types': self.builders,
                            'build_time': current_time_epoch
                        }

                        self.build_manifest[distro][version]['builds'].append(
                            build_info)

                        with open(self.build_manifest_file, 'w') as stream:
                            self.logger.info(
                                'Saving build manifest: %s',
                                self.build_manifest_file)
                            stream.write(json.dumps(
                                self.build_manifest, indent=4))

    def build(self):
        """Build generated Packer template."""

        os.chdir(self.build_dir)

        # Check which of the defined builders are available and only launch
        # those. Values in the dict are:
        # "builder-name" : ["executable", "names"]
        builder_defs = {
            "vmware-iso": [
                "vmware",
                "vmplayer",
                "vmware-vmx"
            ],
            "virtualbox-iso": [
                "virtualbox",
            ],
            "qemu": [
                "qemu-system-x86_64",
            ],
        }
        builders_found = [b if which(builder_exec) else None
                          for b, builder_execs in builder_defs.items()
                          for builder_exec in builder_execs]
        self.logger.info('Builders found: %s', builders_found)

        if self.builder != 'all':
            if self.builder not in builders_found:
                self.logger.error('Builder %s not installed', self.builder)
                sys.exit(1)
            elif self.builder not in self.builders:
                self.logger.error('Builder %s is not defined.', self.builder)
                sys.exit(1)
            else:
                builders_avail = set(self.builder.split()) & set(
                    self.builders) & set(builders_found)
        else:
            builders_avail = set(self.builders) & set(builders_found)

        self.logger.info('Builders avail: %s', builders_avail)

        # We need to account for QEMU and VirtualBox not being able to execute
        # at the same time. If found installed QEMU will run separately. QEMU
        # will more than likely be the one off use case.
        if 'qemu' in builders_avail:
            build_commands = ['packer', 'build',
                              '-only=qemu', 'template.json']
            self.logger.info('Build commands: %s', build_commands)
            self.process(build_commands)
            builders_avail.remove('qemu')

        # Now run everything else
        build_commands = ['packer', 'build',
                          '-only={}'.format(','.join(builders_avail)),
                          'template.json']

        self.logger.info('Build commands: %s', build_commands)
        self.process(build_commands)
        os.chdir(self.current_dir)

    def process(self, build_commands):
        """Process build based on commands passed."""

        build = subprocess.run(build_commands, check=False)

        # Log and exit if failed
        if build.returncode != 0:
            self.logger.error(build)
            sys.exit(1)
        else:
            self.logger.info(build)
