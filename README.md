# packer-builder

## Usage

### Help

```bash
usage: __main__.py [-h] [-d DISTRO] [-f FILE] [-n NUMDAYS] [-o OUTPUTDIR]
                   {build,list-distros}

Packer template builder.

positional arguments:
  {build,list-distros}

optional arguments:
  -h, --help            show this help message and exit
  -d DISTRO, --distro DISTRO
                        Only build distro.
  -f FILE, --file FILE  Path to distro.
  -n NUMDAYS, --numdays NUMDAYS
                        Define number of days since last build.
  -o OUTPUTDIR, --outputdir OUTPUTDIR
                        Define path to save builds.
```

### Example

```bash
python -m packer_builder build -o ~/projects/packer/builds
```
