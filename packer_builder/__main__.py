"""packer_builder/__main__.py"""
import os
from packer_builder.cli import cli_args
from packer_builder.build import Build
from packer_builder.distros import Distros
from packer_builder.generate_templates import GenerateTemplates
from packer_builder.logger import setup_logger


def build(args):
    """Build images."""

    distros = Distros(args).get_distros()
    Build(args, distros)


def list_distros(args):
    """Get distros and display as JSON."""

    distros = Distros(args)
    distros.list_distros()


def generate_templates(args):
    """Generate templates without building."""

    distros = Distros(args).get_distros()
    GenerateTemplates(args, distros).generate()


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

    action_map = {'build': build, 'generate-templates': generate_templates,
                  'list-distros': list_distros}

    action = action_map[args.action]
    action(args)


if __name__ == '__main__':
    main()
