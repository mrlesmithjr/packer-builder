def vsphere_builder(self):
    """VMware specific builder specs."""
    self.builder_spec.update({
        'type': 'vsphere-iso',
        'cluster': '{{ user `vcenter_cluster` }}',
        'convert_to_template': '{{ user `vcenter_convert_to_template` }}',
        'CPUs': '{{ user `cpus` }}',
        'datastore': '{{ user `vcenter_datastore`}}',
        'disk_controller_type': '{{ user `disk_adapter_type` }}',
        'disk_thin_provisioned': True,
        'host': '{{ user `vcenter_host` }}',
        'insecure_connection': 'true',
        'iso_paths': [
            '[{{ user `vcenter_datastore` }}] {{ user `vm_name` }}.iso'
        ],
        'iso_urls': [
            '{{ user `iso_url` }}'
        ],
        'network': '{{ user `vcenter_network` }}',
        'network_card': 'vmxnet3',
        'RAM': '{{ user `memory` }}',
        'RAM_reserve_all': False,
        'password': '{{ user `vcenter_pass` }}',
        'resource_pool': '{{ user `vcenter_resource_pool` }}',
        'username': '{{ user `vcenter_user` }}',
        'vcenter_server': '{{ user `vcenter_server` }}'
    })
    if self.distro == 'alpine':
        guest_os_type = 'other3xLinux64Guest'
    elif self.distro == 'centos':
        guest_os_type = 'centos64Guest'
    elif self.distro == 'debian':
        guest_os_type = 'debian8_64Guest'
    elif self.distro == 'fedora':
        guest_os_type = 'fedora64Guest'
    elif self.distro == 'freenas':
        guest_os_type = 'freebsd64Guest'
    elif self.distro == 'ubuntu':
        guest_os_type = 'ubuntu64Guest'

    self.builder_spec.update({'guest_os_type': guest_os_type})
