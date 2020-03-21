"""packer_builder/specs/builders/vmware.py"""


def vmware_builder(self):
    """VMware specific builder specs."""
    self.builder_spec.update({
        'type': 'vmware-iso',
        'disk_adapter_type': '{{ user `disk_adapter_type` }}',
        'disk_type_id': 0,
        'version': '10',
        'vmx_data': {
            'ethernet0.pciSlotNumber': '32'
        },
        'vmx_remove_ethernet_interfaces': True
    })
    if self.distro == 'alpine':
        guest_os_type = 'other3xlinux-64'
    elif self.distro == 'centos':
        guest_os_type = 'centos-64'
    elif self.distro == 'debian':
        guest_os_type = 'debian8-64'
    elif self.distro == 'fedora':
        guest_os_type = 'fedora-64'
    elif self.distro == 'freenas':
        guest_os_type = 'FreeBSD-64'
        if self.vagrant_box:
            self.builder_spec.update(
                {'disk_additional_size': ['{{ user `disk_size` }}']})
    elif self.distro == 'ubuntu':
        guest_os_type = 'ubuntu-64'

    self.builder_spec.update({'guest_os_type': guest_os_type})
