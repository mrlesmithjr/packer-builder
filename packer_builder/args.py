"""Parse command line arguments."""
import argparse


def get_args():
    """Available command line arguments to pass."""
    parser = argparse.ArgumentParser(description="Packer template builder.")
    parser.add_argument('action', choices=['build', 'list-distros'])
    parser.add_argument('-d', '--distro', help='Only build distro.')
    parser.add_argument('-f', '--file', help='Path to distro.',
                        default='distros.yml', required=False)
    parser.add_argument('-o', '--outputdir',
                        help='Define path to save builds.')
    args = parser.parse_args()
    if args.action == 'build' and args.outputdir is None:
        parser.error('--outputdir is REQUIRED!')
    return args
