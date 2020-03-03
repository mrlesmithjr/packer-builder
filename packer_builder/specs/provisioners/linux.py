def linux_provisioners(self):
    """Linux specific provisioners."""
    # Get list of builders so we can exclude things for specific builders
    builder_types = list()
    for build_type in self.template['builders']:
        builder_types.append(build_type['type'])
    scripts = [
        f'{self.build_scripts_dir}/base.sh',
        f'{self.build_scripts_dir}/virtualbox.sh',
        f'{self.build_scripts_dir}/vmware.sh',
        f'{self.build_scripts_dir}/cleanup.sh',
    ]
    if 'vsphere-iso' not in builder_types:
        scripts.insert(
            len(scripts), f'{self.build_scripts_dir}/zerodisk.sh')
    if self.vagrant_box:
        scripts.insert(
            3, f'{self.build_scripts_dir}/vagrant.sh')
    provisioner_spec = {
        'type': 'shell',
        'scripts': scripts
    }
    self.template['provisioners'].append(provisioner_spec)
