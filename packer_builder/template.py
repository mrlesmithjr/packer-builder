"""Generates the Packer build template."""
import os
import json
import jinja2


class Template():
    """Main Packer template execution."""

    def __init__(self, output_dir, distro, distro_spec, version, version_spec):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.build_dir = output_dir
        self.build_scripts_dir = os.path.join(self.script_dir, 'scripts')
        self.distro = distro.lower()
        self.distro_spec = distro_spec
        self.http_dir = os.path.join(self.build_dir, 'http')
        self.template = dict()
        self.version = version
        self.version_spec = version_spec
        self.get_vars()
        self.get_builders()
        self.get_provisioners()
        self.get_post_processors()
        self.save_template()

    def get_vars(self):
        """Define user specific variables."""
        self.template['variables'] = {
            'cpus': str(self.distro_spec['cpus']),
            'memory': str(self.distro_spec['memory']),
            'disk_adapter_type': self.distro_spec['disk_adapter_type'],
            'disk_size': str(self.distro_spec['disk_size']),
            'iso_checksum': self.version_spec['iso_checksum'],
            'iso_checksum_type': self.version_spec['iso_checksum_type'],
            'iso_url': self.version_spec['iso_url'],
            'username': self.distro_spec['username'],
            'password': self.distro_spec['password'],
            'vm_name': f'{self.distro}-{self.version}',
        }

    def get_builders(self):
        """Direct builder configurations based on builder type."""
        self.template['builders'] = []
        for builder in self.distro_spec['builders']:
            self.builder = builder.lower()
            self.builder_spec = dict()
            self.common_builder()
            self.distro_builder()
            if self.builder == 'qemu':
                self.qemu_builder()
            elif self.builder == 'virtualbox-iso':
                self.virtualbox_builder()
            elif self.builder == 'vmware-iso':
                self.vmware_builder()

            self.template['builders'].append(self.builder_spec)

    def common_builder(self):
        """Common builder specs."""
        self.builder_spec.update({
            'cpus': '{{ user `cpus` }}',
            'disk_size': '{{ user `disk_size` }}',
            'headless': True,
            'http_directory': 'http',
            'iso_checksum_type': '{{ user `iso_checksum_type` }}',
            'iso_checksum': '{{ user `iso_checksum` }}',
            'iso_url': '{{ user `iso_url` }}',
            'memory': '{{ user `memory` }}',
            'output_directory': f'{self.build_dir}''/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}',
            'vm_name': '{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}'
        })
        if self.distro == 'windows':
            self.builder_spec.update({
                'ssh_password': '{{ user `password` }}',
                'ssh_username': '{{ user `username` }}',
                'ssh_timeout': '60m'
            })

    def distro_builder(self):
        """Distro specific builder specs."""
        if not os.path.isdir(self.http_dir):
            os.makedirs(self.http_dir)
        username = self.distro_spec['username']
        password = self.distro_spec['password']
        if self.distro == 'alpine':
            if self.builder == 'qemu':
                disk_dev = 'vda'
            else:
                disk_dev = 'sda'
            bootstrap_cfg = 'answers'
            self.builder_spec.update(
                {
                    'boot_command': [
                        'root<enter><wait><wait><wait>',
                        'ifconfig eth0 up && udhcpc -i eth0<enter><wait10>',
                        'wget http://{{ .HTTPIP }}:{{ .HTTPPort }}/answers<enter><wait>',
                        'sed -i \'s/dev_replace/'f'{disk_dev}''/g\' $PWD/answers<enter>',
                        'setup-alpine -f $PWD/answers<enter><wait5>',
                        '{{ user `password` }}<enter><wait>',
                        '{{ user `password` }}<enter><wait>',
                        '<wait10><wait10><wait10>',
                        'y<enter>',
                        '<wait10><wait10><wait10>',
                        'rc-service sshd stop<enter>',
                        'mount /dev/'f'{disk_dev}''2 /mnt/<enter>',
                        'echo \'PermitRootLogin yes\' >> /mnt/etc/ssh/sshd_config<enter>',
                        'echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /mnt/etc/apk/repositories<enter>',
                        'mount -t proc none /mnt/proc<enter>',
                        'mount -o bind /sys /mnt/sys<enter>',
                        'mount -o bind /dev /mnt/dev<enter>',
                        'chroot /mnt /bin/sh -l<enter>',
                        'apk update<enter><wait>',
                        'apk add bash curl rsyslog ruby shadow sudo<enter><wait>',
                        'gem install facter<enter>',
                        '<wait60><wait60>',
                        'exit<enter><wait10>',
                        'umount /mnt/proc<enter>',
                        'umount /mnt/sys<enter>',
                        'umount /mnt/dev<enter>',
                        'umount /mnt<enter>',
                        'reboot<enter>'
                    ],
                    'shutdown_command': '/sbin/poweroff',
                }
            )
        elif self.distro == 'centos':
            bootstrap_cfg = 'ks.cfg'
            self.builder_spec.update(
                {
                    'boot_command': [
                        '<tab> inst.text ',
                        'inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{bootstrap_cfg}',
                        '<enter><wait>'
                    ],
                    'shutdown_command': '/sbin/halt -h -p',
                }
            )
        elif self.distro == 'debian':
            bootstrap_cfg = 'preseed.cfg'
            self.builder_spec.update(
                {
                    'boot_command': [
                        '<esc><wait>',
                        'install<wait>',
                        ' auto=true',
                        ' priority=critical',
                        ' url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{bootstrap_cfg}',
                        ' <wait><enter>'
                    ],
                    'shutdown_command': 'sudo /sbin/halt -h -p'
                }
            )
        elif self.distro == 'fedora':
            bootstrap_cfg = 'ks.cfg'
            self.builder_spec.update(
                {
                    'boot_command': [
                        '<tab> inst.text ',
                        'inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{bootstrap_cfg}',
                        '<enter><wait>'
                    ],
                    'shutdown_command': '/sbin/halt -h -p',
                }
            )
        elif self.distro == 'freenas':
            bootstrap_cfg = None
            self.builder_spec.update(
                {
                    'boot_command': [
                        '<enter>',
                        '<wait10><wait5>1<enter>',
                        'y',
                        '<wait5><spacebar>o<enter>',
                        '<enter>',
                        '{{ user `password` }}<tab>{{ user `password` }}<tab><enter>',
                        '<enter>',
                        '<wait60><wait60>',
                        '<enter>',
                        '3<enter>',
                        '<wait60><wait60><wait30>',
                        '9<enter>',
                        'curl -X PUT -u {{ user `username` }}:{{ user `password` }} -H \'Content-Type: application/json\' -d \'{\"ssh_rootlogin\": true}\' http://localhost/api/v1.0/services/ssh/<enter>',
                        'curl -X PUT -u {{ user `username` }}:{{ user `password` }} -H \'Content-Type: application/json\' -d \'{\"srv_enable\": true}\' http://localhost/api/v1.0/services/services/ssh/<enter>'
                    ]
                }
            )
        elif self.distro == 'ubuntu':
            bootstrap_cfg = 'preseed.cfg'
            self.builder_spec.update(
                {
                    'boot_command': [
                        '<enter><wait><f6><esc>',
                        '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                        '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                        '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                        '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                        '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                        '<bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs><bs>',
                        '<bs><bs><bs><bs><bs><bs>',
                        '/install/vmlinuz',
                        ' initrd=/install/initrd.gz',
                        ' auto=true',
                        ' priority=critical',
                        ' url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{bootstrap_cfg}',
                        ' <wait><enter>'
                    ],
                    'shutdown_command': 'sudo /sbin/halt -h -p'
                }
            )
        if bootstrap_cfg is not None:
            j2_template_dir = os.path.join(
                self.script_dir, 'http', self.distro)
            j2_template = jinja2.Environment(
                loader=jinja2.FileSystemLoader(j2_template_dir),
                trim_blocks=True)
            bootstrap_template = j2_template.get_template(
                bootstrap_cfg + '.j2').render(username=username, password=password)
            bootstrap_file = os.path.join(self.http_dir, bootstrap_cfg)
            if os.path.isfile(bootstrap_file):
                os.remove(bootstrap_file)
            with open(bootstrap_file, 'w') as bootstrap_cfg:
                bootstrap_cfg.write(bootstrap_template)
                bootstrap_cfg.close()

    def qemu_builder(self):
        """Qemu specific builder specs."""
        self.builder_spec.update({
            'accelerator': 'kvm',
            'type': 'qemu',
            'disk_interface': 'virtio',
            'format': 'qcow2',
        })

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
        elif self.distro == 'ubuntu':
            guest_os_type = 'Ubuntu_64'

        self.builder_spec.update({'guest_os_type': guest_os_type})

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
        elif self.distro == 'ubuntu':
            guest_os_type = 'ubuntu-64'

        self.builder_spec.update({'guest_os_type': guest_os_type})

    def get_provisioners(self):
        """Direct provisioners based on distro type."""
        self.template['provisioners'] = []
        if self.distro == 'freenas':
            self.freenas_provisioners()
        elif self.distro == 'windows':
            self.windows_provisioners()
        else:
            self.linux_provisioners()

    def freenas_provisioners(self):
        provisioner_spec = {
            'type': 'shell',
            'environment_vars': [
                'SSH_USER={{ user `username` }}',
                'SSH_PASS={{ user `password` }}'
            ],
            'scripts': [
                f'{self.build_scripts_dir}/freenas.sh'
            ]
        }
        self.template['provisioners'].append(provisioner_spec)

    def linux_provisioners(self):
        """Linux specific provisioners."""
        provisioner_spec = {
            'type': 'shell',
            'scripts': [
                f'{self.build_scripts_dir}/base.sh',
                f'{self.build_scripts_dir}/virtualbox.sh',
                f'{self.build_scripts_dir}/vmware.sh',
                f'{self.build_scripts_dir}/cleanup.sh',
                f'{self.build_scripts_dir}/zerodisk.sh'
            ]
        }
        self.template['provisioners'].append(provisioner_spec)

    def windows_provisioners(self):
        """Windows specific provisioners."""
        pass

    def get_post_processors(self):
        """Post processors for builds."""
        vmx_file = f'{self.build_dir}''/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}.vmx'
        ovf_file = f'{self.build_dir}''/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}.ovf'
        self.template['post-processors'] = [
            {
                'type': 'shell-local',
                'inline': f'ovftool {vmx_file} {ovf_file}',
                'only': ['vmware-iso']
            }
        ]

    def save_template(self):
        """Save generated template for building."""
        template_json = json.dumps(self.template, indent=4)
        template_file = os.path.join(self.build_dir, 'template.json')
        if os.path.isfile(template_file):
            os.remove(template_file)
        with open(template_file, 'w') as packer_template:
            packer_template.write(template_json)
            packer_template.close()
