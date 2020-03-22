"""packer_builder/specs/builders/common.py"""

# pylint: disable=line-too-long


def common_builder(builder_spec, distro, build_dir):
    """Common builder specs."""

    builder_spec.update({
        'cpus': '{{ user `cpus` }}',
        'disk_size': '{{ user `disk_size` }}',
        'headless': True,
        'http_directory': 'http',
        'iso_checksum_type': '{{ user `iso_checksum_type` }}',
        'iso_checksum': '{{ user `iso_checksum` }}',
        'iso_url': '{{ user `iso_url` }}',
        'memory': '{{ user `memory` }}',
        'output_directory': f'{build_dir}''/{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}',  # noqa: E501
        'vm_name': '{{ user `vm_name` }}-{{ build_type }}-{{ timestamp }}'
    })

    if distro != 'windows':
        builder_spec.update({
            'ssh_password': '{{ user `password` }}',
            'ssh_username': '{{ user `username` }}',
            'ssh_timeout': '60m'
        })

    return builder_spec
