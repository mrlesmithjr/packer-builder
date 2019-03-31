"""Build generated Packer template."""
import os
from datetime import datetime
import time
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
        for distro, distro_spec in self.distros.items():
            distro_check = self.build_manifest.get(distro)
            if distro_check is None:
                self.build_manifest[distro] = {'builds': []}
            if self.distro == 'all' or (self.distro != 'all' and
                                        self.distro == distro):
                for version, version_spec in distro_spec['versions'].items():
                    Template(self.build_dir, distro, distro_spec,
                             version, version_spec)
                    self.builders = distro_spec['builders']
                    self.current_dir = os.getcwd()
                    self.validate()
                    build_time_epoch = time.mktime(
                        datetime.now().timetuple())
                    build_info = {'version': str(version),
                                  'build_time': str(build_time_epoch)}
                    self.build_manifest[distro]['builds'].append(
                        build_info)
                    self.build()
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
        if 'qemu' in self.builders and 'virtualbox-iso' in self.builders:
            build = subprocess.Popen(
                ['packer', 'build', '-parallel=false', 'template.json'])
        else:
            build = subprocess.Popen(
                ['packer', 'build', 'template.json'])
        build.wait()
        if build.returncode != 0:
            sys.exit(1)
        os.chdir(self.current_dir)
