"""packer_builder/specs/provisioners/freenas.py"""

# pylint: disable=line-too-long


def freenas_provisioners(self):
    """FreeNAS specific provisioners."""
    scripts = []
    if self.vagrant_box:
        scripts.append(f'{self.build_scripts_dir}/freenas.sh')
    provisioner_spec = {
        'type': 'shell',
        'environment_vars': [
            'SSH_USER={{ user `username` }}',
            'SSH_PASS={{ user `password` }}'
        ],
        'scripts': scripts
    }
    self.template['provisioners'].append(provisioner_spec)
