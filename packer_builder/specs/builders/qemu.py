"""packer_builder/specs/builders/qemu.py"""

import subprocess
from shutil import which
from sys import platform


def qemu_builder(**kwargs):
    """Qemu specific builder specs."""

    # Setup vars from kwargs
    builder_spec = kwargs['data']['builder_spec']

    # Check which platform QEMU is running on to set accelerator correctly
    # https://www.packer.io/docs/builders/qemu.html#accelerator
    if platform in ('linux', 'linux2'):
        if which('kvm-ok'):
            process = subprocess.Popen(["kvm-ok"])
            process.wait()
            if process.returncode == 0:
                accelerator = 'kvm'
            else:
                accelerator = 'tcg'
        else:
            with open('/proc/cpuinfo') as cpuinfo:
                if 'vmx' in cpuinfo.read():
                    accelerator = 'kvm'
                elif 'svm' in cpuinfo.read():
                    accelerator = 'kvm'
                else:
                    accelerator = 'tcg'
    elif platform == "darwin":
        accelerator = 'hvf'
    else:
        accelerator = 'none'

    builder_spec.update({
        'accelerator': accelerator,
        'type': 'qemu',
        'disk_interface': 'virtio',
        'format': 'qcow2',
    })

    return builder_spec
