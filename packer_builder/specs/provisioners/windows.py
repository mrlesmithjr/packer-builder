"""packer_builder/specs/provisioners/windows.py"""


def windows_provisioners(**kwargs):
    """Windows specific provisioners."""

    # Setup vars from kwargs
    # vagrant_box = kwargs['data']['vagrant_box']
    # build_scripts_dir = kwargs['data']['build_scripts_dir']
    template = kwargs['data']['template']

    return template
