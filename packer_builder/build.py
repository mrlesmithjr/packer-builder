"""Build generated Packer template."""
import os
import logging
from datetime import datetime
import time
import subprocess
import sys
import json
from shutil import which
from packer_builder.template import Template


# pylint: disable=too-many-instance-attributes
class Build():
    """Main builder process."""

    def __init__(self, args, distros):
        self.logger = logging.getLogger(__name__)
        self.distros = distros
        self.build_dir = args.outputdir
        self.logger.debug('Build dir: %s', self.build_dir)
        self.build_manifest_file = os.path.join(
            self.build_dir, 'packer-builder.json')
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
                self.logger.debug(
                    'Loading build manifest: %s', self.build_manifest_file)
                self.build_manifest = json.load(stream)
        else:
            self.build_manifest = dict()

# pylint: disable=too-many-locals
    def iterate(self):
        """Iterate through defined distros and build them."""
        self.current_dir = os.getcwd()
        self.logger.debug('Current directory: %s', self.current_dir)
        for distro, distro_spec in self.distros.items():
            self.logger.debug('Distro: %s', distro)
            self.logger.debug('Distro spec: %s', distro_spec)
            self.builders = distro_spec['builders']
            distro_check = self.build_manifest.get(distro)
            self.logger.debug('Distro check: %s', distro_check)
            if distro_check is None:
                self.build_manifest[distro] = dict()
            if self.distro == 'all' or (self.distro != 'all' and
                                        self.distro == distro):
                for version, version_spec in distro_spec['versions'].items():
                    version = str(version)
                    version_check = self.build_manifest[distro].get(version)
                    self.logger.debug('Version %s check: %s',
                                      version, version_check)
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
                    self.logger.debug('Build image: %s', build_image)
                    if build_image:
                        Template(self.build_dir, self.password_override,
                                 distro, distro_spec, version, version_spec)
                        self.validate()
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
                            self.logger.debug(
                                'Saving build manifest: %s',
                                self.build_manifest_file)
                            stream.write(json.dumps(
                                self.build_manifest, indent=4))

    def validate(self):
        """Validate generated Packer template."""
        os.chdir(self.build_dir)
        validate = subprocess.Popen(['packer', 'validate', 'template.json'])
        validate.wait()
        self.logger.debug(
            'Template validation returncode: %s', validate.returncode)
        if validate.returncode != 0:
            sys.exit(1)
        os.chdir(self.current_dir)

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
        self.logger.debug('Builders found: %s', builders_found)
        if self.builder != 'all':
            if self.builder not in builders_found:
                print("Builder {0} not installed.".format(self.builder))
                sys.exit(1)
            elif self.builder not in self.builders:
                print("Builder {0} is not defined.".format(self.builder))
                sys.exit(1)
            else:
                builders_avail = set(self.builder.split()) & set(
                    self.builders) & set(builders_found)
        else:
            builders_avail = set(self.builders) & set(builders_found)
        self.logger.debug('Builders avail: %s', builders_avail)
        # We need to account for QEMU and VirtualBox not being able to execute
        # at the same time. If found installed QEMU will run separately. QEMU
        # will more than likely be the one off use case.
        if 'qemu' in builders_avail:
            build_commands = ['packer', 'build',
                              '-only=qemu', 'template.json']
            self.logger.debug('Build commands: %s', build_commands)
            self.process_build(build_commands)
            builders_avail.remove('qemu')
        # Now run everything else
        build_commands = ['packer', 'build',
                          '-only={}'.format(','.join(builders_avail)),
                          'template.json']
        self.logger.debug('Build commands: %s', build_commands)
        self.process_build(build_commands)
        os.chdir(self.current_dir)

    def process_build(self, build_commands):
        """Process build based on commands passed."""
        build = subprocess.Popen(build_commands)
        build.wait()
        self.logger.debug('Build returncode: %s', build.returncode)
        if build.returncode != 0:
            sys.exit(1)
