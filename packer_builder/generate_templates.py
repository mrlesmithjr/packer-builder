import os
import shutil
from packer_builder.template import Template
from packer_builder.build import Build


class GenerateTemplates():

    def __init__(self, args, distros):
        self.distros = distros
        self.build_dir = args.outputdir
        self.current_dir = os.getcwd()
        self.generate()

    def generate(self):
        for distro, distro_spec in self.distros.items():
            for version, version_spec in distro_spec['versions'].items():
                version = str(version)
                Template(self.build_dir, distro, distro_spec,
                         version, version_spec)
                Build.validate(self)
                generated_template = os.path.join(
                    self.build_dir, 'template.json')
                renamed_template = os.path.join(
                    self.build_dir, f'{distro}-{version}.json')
                shutil.move(generated_template, renamed_template)
