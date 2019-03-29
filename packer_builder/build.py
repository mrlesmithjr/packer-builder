"""Build generated Packer template."""
import os
import subprocess
import sys
from .template import Template


class Build():
    """Main builder process."""

    def __init__(self, output_dir, distros):
        self.distros = distros
        self.build_dir = output_dir
        self.iterate()

    def iterate(self):
        """Iterate through defined distros and build them."""
        for distro, distro_spec in self.distros.items():
            for version, version_spec in distro_spec['versions'].items():
                Template(self.build_dir, distro, distro_spec,
                         version, version_spec)
                self.builders = distro_spec['builders']
                self.current_dir = os.getcwd()
                self.validate()
                self.build()

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
