import json
from .args import get_args
from .build import Build
from .distros import Distros
from .template import Template

ARGS = get_args()
DISTROS = Distros(ARGS).get_distros()
OUTPUT_DIR = ARGS.outputdir
for distro, distro_spec in DISTROS.items():
    for version, version_spec in distro_spec['versions'].items():
        builder = Template(OUTPUT_DIR, distro, distro_spec, version,
                           version_spec).builder()
        Build(distro_spec, builder)
