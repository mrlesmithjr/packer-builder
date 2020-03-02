def debian_spec(self):
    self.bootstrap_cfg = 'preseed.cfg'
    self.builder_spec.update(
        {
            'boot_command': [
                '<esc><wait>',
                'install<wait>',
                ' auto=true',
                '<wait>',
                ' priority=critical',
                '<wait>',
                ' url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{self.distro}-{self.version}-{self.bootstrap_cfg}',
                ' <wait><enter>'
            ],
            'boot_wait': '30s',
            'shutdown_command': 'sudo /sbin/halt -h -p'
        }
    )
