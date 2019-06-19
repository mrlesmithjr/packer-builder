# packer-builder

## Usage

### Help

```bash
python -m packer_builder --help
...
usage: __main__.py [-h] [-d DISTRO] [-b BUILDER] [-f FILE] [-n NUMDAYS]
                   [-o OUTPUTDIR]
                   {build,generate-templates,list-distros,update-metadata}

Packer builder.

positional arguments:
  {build,generate-templates,list-distros,update-metadata}

optional arguments:
  -h, --help            show this help message and exit
  -d DISTRO, --distro DISTRO
                        Only build specific distro.
  -b BUILDER, --builder BUILDER
                        Only use specific builder.
  -f FILE, --file FILE  Path to distro.
  -n NUMDAYS, --numdays NUMDAYS
                        Define number of days since last build.
  -o OUTPUTDIR, --outputdir OUTPUTDIR
                        Define path to save builds.
```

### Examples

```bash
python -m packer_builder build -o ~/projects/packer/builds
```

#### Generate Templates (ONLY)

```bash
python -m packer_builder generate-templates --outputdir ~/projects/packer
```
