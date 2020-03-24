"""packer_builder/specs/builders/vmware.py"""


def vmware_builder(**kwargs):
    """VMware specific builder specs."""

    # Setup vars from kwargs
    builder_spec = kwargs['data']['builder_spec']
    distro = kwargs['data']['distro']
    vagrant_box = kwargs['data']['vagrant_box']

    builder_spec.update({
        'type': 'vmware-iso',
        'disk_adapter_type': '{{ user `disk_adapter_type` }}',
        'disk_type_id': 0,
        'version': '10',
        'vmx_data': {
            'ethernet0.pciSlotNumber': '32'
        },
        'vmx_remove_ethernet_interfaces': True
    })

    # Define OS type map for distro to guest OS type
    os_type_map = {'alpine': 'other3xlinux-64', 'centos': 'centos-64',
                   'debian': 'debian8-64', 'fedora': 'fedora-64',
                   'freenas': 'FreeBSD-64', 'ubuntu': 'ubuntu-64'}

    # Lookup distro OS type
    guest_os_type = os_type_map[distro]

    # If FreeNAS, add storage devices if Vagrant to ensure we can provision
    if distro == 'freenas' and vagrant_box:
        builder_spec.update(
            {'disk_additional_size': ['{{ user `disk_size` }}']})

    builder_spec.update({'guest_os_type': guest_os_type})

    return builder_spec
