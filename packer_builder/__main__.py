"""An easy way to define and build Packer images."""
import os
from packer_builder.cli import cli_args
from packer_builder.build import Build
from packer_builder.distros import Distros
from packer_builder.generate_templates import GenerateTemplates
from packer_builder.logger import setup_logger



def main():
    """Packer builder main execution."""

    # Setup root logger
    setup_logger()

    # Capture CLI arguments
    args = cli_args()

    # Ensure output dir exists if defined
    if args.outputdir is not None:
        if not os.path.isdir:
            os.makedirs(args.outputdir)

    if args.action == 'build':
        Build(args, distros)
    elif args.action == 'list-distros':
        Distros(args).list_distros()
    elif args.action == 'generate-templates':
        GenerateTemplates(args, distros)


if __name__ == '__main__':
    main()
