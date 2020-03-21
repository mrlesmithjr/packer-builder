"""packer_builder/specs/builders/distro.py"""

import os
import jinja2
from packer_builder.specs.builders.distros.alpine import alpine_spec
from packer_builder.specs.builders.distros.centos import centos_spec
from packer_builder.specs.builders.distros.debian import debian_spec
from packer_builder.specs.builders.distros.fedora import fedora_spec
from packer_builder.specs.builders.distros.freenas import freenas_spec
from packer_builder.specs.builders.distros.ubuntu import ubuntu_spec


def distro_builder(self):
    """Distro specific builder specs."""
    if not os.path.isdir(self.http_dir):
        os.makedirs(self.http_dir)
    username = self.distro_spec['username']
    password = self.distro_spec['password']
    if self.distro == 'alpine':
        alpine_spec(self)
    elif self.distro == 'centos':
        centos_spec(self)
    elif self.distro == 'debian':
        debian_spec(self)
    elif self.distro == 'fedora':
        fedora_spec(self)
    elif self.distro == 'freenas':
        freenas_spec(self)
    elif self.distro == 'ubuntu':
        ubuntu_spec(self)

    if self.bootstrap_cfg is not None:
        j2_template_dir = os.path.join(
            self.script_dir, 'http', self.distro)
        j2_template = jinja2.Environment(
            loader=jinja2.FileSystemLoader(j2_template_dir),
            trim_blocks=True)
        bootstrap_template = j2_template.get_template(
            self.bootstrap_cfg + '.j2').render(username=username,
                                               password=password)
        bootstrap_file = os.path.join(
            self.http_dir,
            f'{self.distro}-{self.version}-{self.bootstrap_cfg}')
        if os.path.isfile(bootstrap_file):
            os.remove(bootstrap_file)
        with open(bootstrap_file, 'w') as bootstrap_cfg:
            bootstrap_cfg.write(bootstrap_template)
            bootstrap_cfg.close()
