"""packer_builder/specs/builder/distros/debian.py"""

# pylint: disable=line-too-long


def debian_spec(self):
    "Debian specs."
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
                ' url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{self.distro}-{self.version}-{self.bootstrap_cfg}',  # noqa: E501
                ' <wait><enter>'
            ],
            'boot_wait': '30s',
            'shutdown_command': 'sudo /sbin/halt -h -p'
        }
    )
