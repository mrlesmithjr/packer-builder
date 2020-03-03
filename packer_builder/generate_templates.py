"""Generate Packer templates for offline execution/review."""
import os
import shutil
from packer_builder.template import Template
from packer_builder.build import Build
from packer_builder.logger import get_logger


# pylint: disable=too-few-public-methods
class GenerateTemplates():
    """Generate Packer templates without building."""

    def __init__(self, args, distros):
        self.logger = get_logger(__name__)
        self.distros = distros
        self.build_dir = args.outputdir
        self.password_override = args.password
        self.current_dir = os.getcwd()
        self.generate()

    def generate(self):
        """Generate templates and rename them into the defined output dir."""

        # Iterate through defined distros
        for distro, distro_spec in self.distros.items():
            # Iterate through versions defined in distros
            for version, version_spec in distro_spec['versions'].items():
                version = str(version)
                # Generate the template
                Template(self.build_dir, self.password_override,
                         distro, distro_spec, version, version_spec)
                # Validate the generated template
                Build.validate(self)
                generated_template = os.path.join(
                    self.build_dir, 'template.json')
                renamed_template = os.path.join(
                    self.build_dir, f'{distro}-{version}.json')  # noqa: E999
                # Rename the generated template
                shutil.move(generated_template, renamed_template)
