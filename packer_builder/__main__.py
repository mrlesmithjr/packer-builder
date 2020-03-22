"""packer_builder/__main__.py"""
import os
from packer_builder.cli import cli_args
from packer_builder.build import Build
from packer_builder.distros import Distros
from packer_builder.templates import Templates
from packer_builder.logger import setup_logger


def build(args):
    """Build images."""

    # Get dictionary of distros
    distros = Distros(args).get_distros()
    # Build all distros
    Build(args, distros)


def list_distros(args):
    """Get distros and display as JSON."""

    # Get dictionary of distros
    distros = Distros(args)
    # List all distros as JSON output
    distros.list_distros()


def generate_templates(args):
    """Generate templates without building."""

    # Get dictionary of distros
    distros = Distros(args).get_distros()
    # Generate all templates without building
    templates = Templates(args, distros)
    templates.generate()


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

    # Map actions to respective functions
    action_map = {'build': build, 'generate-templates': generate_templates,
                  'list-distros': list_distros}

    # Lookup action from map
    action = action_map[args.action]
    # Execute action
    action(args)


if __name__ == '__main__':
    main()
