"""An easy way to define and build Packer images."""
from .args import get_args
from .build import Build
from .distros import Distros


def main():
    """Packer builder main execution."""
    args = get_args()
    distros = Distros(args).get_distros()
    output_dir = args.outputdir
    Build(output_dir, distros)


if __name__ == '__main__':
    main()
