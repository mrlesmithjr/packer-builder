"""packer_builder/specs/builder/distros/ubuntu.py"""


# pylint: disable=line-too-long
def ubuntu_spec(**kwargs):
    """Ubuntu specs."""

    # Setup vars from kwargs
    builder_spec = kwargs['data']['builder_spec']
    distro = kwargs['data']['distro']
    version = kwargs['data']['version']

    bootstrap_cfg = 'preseed.cfg'
    builder_spec.update(
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
                ' url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{distro}-{version}-{bootstrap_cfg}',  # noqa: E501
                ' <wait><enter>'
            ],
            'boot_wait': '30s',
            'shutdown_command': 'sudo /sbin/halt -h -p'
        }
    )

    return bootstrap_cfg, builder_spec
