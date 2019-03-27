"""Parse command line arguments."""
import argparse


def get_args():
    """Available command line arguments to pass."""
    parser = argparse.ArgumentParser(description="Packer template builder.")
    parser.add_argument('-f', '--file', help='Path to distro ',
                        default='distros.yml', required=True)
    parser.add_argument('-o', '--outputdir', required=True)
    args = parser.parse_args()
    return args
