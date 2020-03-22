"""packer_builder/specs/builders/virtualbox.py"""


def virtualbox_builder(**kwargs):
    """Virtualbox specific builder specs."""

    # Setup vars from kwargs
    builder_spec = kwargs['data']['builder_spec']
    distro = kwargs['data']['distro']
    vagrant_box = kwargs['data']['vagrant_box']

    builder_spec.update({
        'type': 'virtualbox-iso',
        'hard_drive_interface': '{{ user `disk_adapter_type` }}',
    })

    # Define OS type map for distro to guest OS type
    os_type_map = {'alpine': 'Linux26_64', 'centos': 'RedHat_64',
                   'debian': 'Debian_64', 'fedora': 'Fedora_64',
                   'freenas': 'FreeBSD_64', 'ubuntu': 'Ubuntu_64'}

    # Lookup distro OS type
    guest_os_type = os_type_map[distro]

    # If FreeNAS, add storage devices if Vagrant to ensure we can provision
    if distro == 'freenas' and vagrant_box:
        builder_spec.update(
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

    builder_spec.update({'guest_os_type': guest_os_type})

    return builder_spec
