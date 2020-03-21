"""packer_builder/specs/builder/distros/centos.py"""


# pylint: disable=line-too-long
def centos_spec(self):
    """CentOS specs."""
    self.bootstrap_cfg = 'ks.cfg'
    self.builder_spec.update(
        {
            'boot_command': [
                '<tab> inst.text ',
                'inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{self.distro}-{self.version}-{self.bootstrap_cfg}',  # noqa: E501
                '<enter><wait>'
            ],
            'boot_wait': '30s',
            'shutdown_command': '/sbin/halt -h -p',
        }
    )
