import yaml


class Distros():
    def __init__(self, ARGS):
        self.file = ARGS.file
        self.distros = dict()
        self.load_file()
        self.parse_file()

    def load_file(self):
        with open(self.file, 'r') as file:
            self.data = yaml.load(file, Loader=yaml.FullLoader)

    def parse_file(self):
        for key, value in self.data.items():
            self.distros[key] = value

    def get_distros(self):
        return self.distros
