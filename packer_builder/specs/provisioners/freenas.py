"""packer_builder/specs/provisioners/freenas.py"""

# pylint: disable=line-too-long


def freenas_provisioners(**kwargs):
    """FreeNAS specific provisioners."""

    scripts = []

    # Setup vars from kwargs
    vagrant_box = kwargs['data']['vagrant_box']
    build_scripts_dir = kwargs['data']['build_scripts_dir']
    template = kwargs['data']['template']

    if vagrant_box:
        scripts.append(f'{build_scripts_dir}/freenas.sh')

    provisioner_spec = {
        'type': 'shell',
        'environment_vars': [
            'SSH_USER={{ user `username` }}',
            'SSH_PASS={{ user `password` }}'
        ],
        'scripts': scripts
    }

    template['provisioners'].append(provisioner_spec)

    return template
