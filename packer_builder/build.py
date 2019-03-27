"""Build generated Packer template."""
import os
import subprocess
import sys


class Build():
    def __init__(self, distro_spec, builder):
        self.builders = distro_spec['builders']
        self.path = builder['path']
        self.current_dir = os.getcwd()
        self.validate()
        self.build()

    def validate(self):
        """Validate generated Packer template."""
        os.chdir(self.path)
        validate = subprocess.Popen(['packer', 'validate', 'template.json'])
        validate.wait()
        if validate.returncode != 0:
            sys.exit(1)
        os.chdir(self.current_dir)

    def build(self):
        """Build generated Packer template."""
        os.chdir(self.path)
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
