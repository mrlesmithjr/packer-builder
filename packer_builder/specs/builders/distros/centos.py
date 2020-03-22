"""packer_builder/specs/builder/distros/centos.py"""


# pylint: disable=line-too-long
def centos_spec(**kwargs):
    """CentOS specs."""

    # Setup vars from kwargs
    builder_spec = kwargs['data']['builder_spec']
    distro = kwargs['data']['distro']
    version = kwargs['data']['version']

    bootstrap_cfg = 'ks.cfg'
    builder_spec.update(
        {
            'boot_command': [
                '<tab> inst.text ',
                'inst.ks=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{distro}-{version}-{bootstrap_cfg}',  # noqa: E501
                '<enter><wait>'
            ],
            'boot_wait': '30s',
            'shutdown_command': '/sbin/halt -h -p',
        }
    )

    return bootstrap_cfg, builder_spec
