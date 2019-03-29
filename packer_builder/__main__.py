"""An easy way to define and build Packer images."""
from .args import get_args
from .build import Build
from .distros import Distros


def main():
    """Packer builder main execution."""
    args = get_args()
    distros = Distros(args).get_distros()
    if args.action == 'build':
        Build(args, distros)
    elif args.action == 'list-distros':
        Distros(args).list_distros()


if __name__ == '__main__':
    main()
