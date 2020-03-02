def linux_provisioners(self):
    """Linux specific provisioners."""
    scripts = [
        f'{self.build_scripts_dir}/base.sh',
        f'{self.build_scripts_dir}/virtualbox.sh',
        f'{self.build_scripts_dir}/vmware.sh',
        f'{self.build_scripts_dir}/cleanup.sh',
        f'{self.build_scripts_dir}/zerodisk.sh'
    ]
    if self.vagrant_box:
        scripts.insert(
            3, f'{self.build_scripts_dir}/vagrant.sh')
    provisioner_spec = {
        'type': 'shell',
        'scripts': scripts
    }
    self.template['provisioners'].append(provisioner_spec)
