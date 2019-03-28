"""An easy way to define and build Packer images."""
from .args import get_args
from .build import Build
from .distros import Distros

ARGS = get_args()
DISTROS = Distros(ARGS).get_distros()
OUTPUT_DIR = ARGS.outputdir
Build(OUTPUT_DIR, DISTROS)
