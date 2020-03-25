"""packer_builder/specs/builder/distros/alpine.py"""


# pylint: disable=line-too-long
def alpine_spec(**kwargs):
    """Alpine specs."""

    # Setup vars from kwargs
    builder = kwargs['data']['builder']
    builder_spec = kwargs['data']['builder_spec']
    distro = kwargs['data']['distro']
    version = kwargs['data']['version']

    if builder == 'qemu':
        disk_dev = 'vda'
    else:
        disk_dev = 'sda'

    bootstrap_cfg = 'answers'

    builder_spec.update(
        {
            'boot_command': [
                'root<enter><wait><wait><wait>',
                'ifconfig eth0 up && udhcpc -i eth0<enter><wait10>',
                'wget http://{{ .HTTPIP }}:{{ .HTTPPort }}/'f'{distro}-{version}-answers<enter><wait>',  # noqa: E501
                f'sed -i \'s/dev_replace/{disk_dev}/g\' 'f'$PWD/{distro}-{version}-answers<enter>',  # noqa: E501
                f'setup-alpine -f $PWD/{distro}-{version}-answers<enter><wait5>',  # noqa: E501
                '{{ user `password` }}<enter><wait>',
                '{{ user `password` }}<enter><wait>',
                '<wait10><wait10><wait10>',
                'y<enter>',
                '<wait10><wait10><wait10>',
                'rc-service sshd stop<enter>',
                'mount /dev/'f'{disk_dev}''2 /mnt/<enter>',
                'echo \'PermitRootLogin yes\' >> /mnt/etc/ssh/sshd_config<enter>',  # noqa: E501
                'echo http://dl-cdn.alpinelinux.org/alpine/edge/community >> /mnt/etc/apk/repositories<enter>',  # noqa: E501
                'mount -t proc none /mnt/proc<enter>',
                'mount -o bind /sys /mnt/sys<enter>',
                'mount -o bind /dev /mnt/dev<enter>',
                'chroot /mnt /bin/sh -l<enter>',
                'apk update<enter><wait>',
                'apk add bash curl rsyslog ruby shadow sudo<enter><wait>',
                '<wait60><wait60>',
                'exit<enter><wait10>',
                'umount /mnt/proc<enter>',
                'umount /mnt/sys<enter>',
                'umount /mnt/dev<enter>',
                'umount /mnt<enter>',
                'reboot<enter>'
            ],
            'boot_wait': '30s',
            'shutdown_command': '/sbin/poweroff',
        }
    )

    return bootstrap_cfg, builder_spec
