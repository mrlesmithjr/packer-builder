def virtualbox_builder(self):
    """Virtualbox specific builder specs."""
    self.builder_spec.update({
        'type': 'virtualbox-iso',
        'hard_drive_interface': '{{ user `disk_adapter_type` }}',
    })
    if self.distro == 'alpine':
        guest_os_type = 'Linux26_64'
    elif self.distro == 'centos':
        guest_os_type = 'RedHat_64'
    elif self.distro == 'debian':
        guest_os_type = 'Debian_64'
    elif self.distro == 'fedora':
        guest_os_type = 'Fedora_64'
    elif self.distro == 'freenas':
        guest_os_type = 'FreeBSD_64'
        if self.vagrant_box:
            self.builder_spec.update(
                {
                    'vboxmanage': [
                        [
                            'createhd',
                            '--format',
                            'VDI',
                            '--filename',
                            'disk2.vdi',
                            '--size',
                            '{{ user `disk_size` }}'
                        ],
                        [
                            'storageattach',
                            '{{ .Name }}',
                            '--storagectl',
                            'SCSI Controller',
                            '--port',
                            '1',
                            '--device',
                            '0',
                            '--type',
                            'hdd',
                            '--medium',
                            'disk2.vdi'
                        ]
                    ]
                })
    elif self.distro == 'ubuntu':
        guest_os_type = 'Ubuntu_64'

    self.builder_spec.update({'guest_os_type': guest_os_type})
