"""packer_builder/cli.py"""

import argparse
from packer_builder.release import __package_name__, __version__


def cli_args():
    """Console script for packer_builder."""
    parser = argparse.ArgumentParser(description="Packer builder.")
    parser.add_argument('action', choices=[
        'build', 'generate-templates', 'list-distros',
        'update-metadata'])
    parser.add_argument('-d', '--distro', help='Only build specific distro.')
    parser.add_argument('-b', '--builder', help='Only use specific builder.')
    parser.add_argument(
        '-f', '--file', help='Path to distro.', default='distros.yml')
    parser.add_argument('-n', '--numdays',
                        help='Define number of days since last build.',
                        default=30)
    parser.add_argument('-o', '--outputdir',
                        help='Define path to save builds.')
    parser.add_argument('-p', '--password',
                        help='Define default password to override distros.yml')

    parser.add_argument('--version', action='version',
                        version=f'{__package_name__} {__version__}')
    args = parser.parse_args()
    if (args.action in ['build', 'generate-templates'] and
            args.outputdir is None):
        parser.error('--outputdir is REQUIRED!')

    return args
