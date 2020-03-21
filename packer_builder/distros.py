"""Load distros YAML file for parsing."""
import logging
import json
import yaml


class Distros():
    """Main execution of loading and parsing distros YAML file."""

    def __init__(self, args):
        self.file = args.file
        # Setup logging
        self.logger = logging.getLogger(__name__)
        self.distros = dict()
        self.load_file()
        self.parse_file()

    def load_file(self):
        """Load distros YAML file for parsing."""
        self.logger.info('Loading: %s', self.file)
        with open(self.file, 'r') as file:
            self.data = yaml.load(file, Loader=yaml.FullLoader)

    def parse_file(self):
        """Parse distros YAML file."""
        self.logger.info('Parsing: %s', self.data)
        for key, value in self.data.items():
            self.distros[key] = value

    def get_distros(self):
        """Get distros found in YAML file."""
        return self.distros

    def list_distros(self):
        """Return list of distros available."""
        for distro in self.distros:
            print(distro)
