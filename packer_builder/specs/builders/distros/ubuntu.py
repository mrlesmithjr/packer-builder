def ubuntu_spec(self):
    self.bootstrap_cfg = 'preseed.cfg'
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
                ' url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{self.distro}-{self.version}-{self.bootstrap_cfg}',
                ' <wait><enter>'
            ],
            'boot_wait': '30s',
            'shutdown_command': 'sudo /sbin/halt -h -p'
        }
    )
