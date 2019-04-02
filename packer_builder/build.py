"""Build generated Packer template."""
import os
from datetime import datetime
import time
import shutil
import subprocess
import sys
import json
from .template import Template


class Build():
    """Main builder process."""

    def __init__(self, args, distros):
        self.distros = distros
        self.build_dir = args.outputdir
        self.build_manifest_file = os.path.join(
            self.build_dir, 'packer-builder.json')
        self.num_days = args.numdays
        if args.distro is not None:
            self.distro = args.distro
        else:
            self.distro = 'all'
        self.load_build_manifest()
        self.iterate()

    def load_build_manifest(self):
        if os.path.isfile(self.build_manifest_file):
            with open(self.build_manifest_file, 'r') as stream:
                self.build_manifest = json.load(stream)
        else:
            self.build_manifest = dict()

    def iterate(self):
        """Iterate through defined distros and build them."""
        self.current_dir = os.getcwd()
        for distro, distro_spec in self.distros.items():
            self.builders = distro_spec['builders']
            distro_check = self.build_manifest.get(distro)
            if distro_check is None:
                self.build_manifest[distro] = dict()
            if self.distro == 'all' or (self.distro != 'all' and
                                        self.distro == distro):
                for version, version_spec in distro_spec['versions'].items():
                    version = str(version)
                    version_check = self.build_manifest[distro].get(version)
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
                    if build_image:
                        Template(self.build_dir, distro, distro_spec,
                                 version, version_spec)
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
                            stream.write(json.dumps(
                                self.build_manifest, indent=4))

    def validate(self):
        """Validate generated Packer template."""
        os.chdir(self.build_dir)
        validate = subprocess.Popen(['packer', 'validate', 'template.json'])
        validate.wait()
        if validate.returncode != 0:
            sys.exit(1)
        os.chdir(self.current_dir)

    def build(self):
        """Build generated Packer template."""
        os.chdir(self.build_dir)
        # We need to account for QEMU and VirtualBox not being able to execute
        # at the same time.
        if 'qemu' in self.builders and 'virtualbox-iso' in self.builders:
            # Check to ensure QEMU is installed. This may not always be the
            # case. If not found installed we will skip the QEMU builder. QEMU
            # will more than likely be the one off use case.
            qemu_check = shutil.which('qemu-system-x86_64')
            if qemu_check is not None:
                build_commands = ['packer', 'build',
                                  '-only=qemu', 'template.json']
                self.process_build(build_commands)
                build_commands = ['packer', 'build',
                                  '-except=qemu', 'template.json']
                self.process_build(build_commands)
            else:
                print('QEMU/KVM not installed. Skipping....')
                build_commands = ['packer', 'build',
                                  '-except=qemu', 'template.json']
                self.process_build(build_commands)
        else:
            build_commands = ['packer', 'build', 'template.json']
            self.process_build(build_commands)
        os.chdir(self.current_dir)

    def process_build(self, build_commands):
        """Process build based on commands passed."""
        build = subprocess.Popen(build_commands)
        build.wait()
        if build.returncode != 0:
            sys.exit(1)
