"""packer_builder/specs/provisioners/linux.py"""


def linux_provisioners(**kwargs):
    """Linux specific provisioners."""

    # Setup vars from kwargs
    vagrant_box = kwargs['data']['vagrant_box']
    build_scripts_dir = kwargs['data']['build_scripts_dir']
    template = kwargs['data']['template']

    scripts = [
        f'{build_scripts_dir}/base.sh',
        f'{build_scripts_dir}/virtualbox.sh',
        f'{build_scripts_dir}/vmware.sh',
        f'{build_scripts_dir}/cleanup.sh',
        f'{build_scripts_dir}/zerodisk.sh'
    ]
    if vagrant_box:
        scripts.insert(
            3, f'{build_scripts_dir}/vagrant.sh')
    provisioner_spec = {
        'type': 'shell',
        'scripts': scripts
    }
    template['provisioners'].append(provisioner_spec)

    return template
