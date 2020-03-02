import subprocess
from shutil import which
from sys import platform


def qemu_builder(self):
    """Qemu specific builder specs."""

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

    self.builder_spec.update({
        'accelerator': accelerator,
        'type': 'qemu',
        'disk_interface': 'virtio',
        'format': 'qcow2',
    })
