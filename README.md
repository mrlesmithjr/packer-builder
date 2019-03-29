# packer-builder

## Usage

### Help

```bash
python -m packer_builder --help
...
usage: __main__.py [-h] [-d DISTRO] [-f FILE] -o OUTPUTDIR
                   {build,list-distros}

Packer template builder.

positional arguments:
  {build,list-distros}

optional arguments:
  -h, --help            show this help message and exit
  -d DISTRO, --distro DISTRO
                        Only build distro.
  -f FILE, --file FILE  Path to distro.
  -o OUTPUTDIR, --outputdir OUTPUTDIR
                        Define path to save builds.
```

### Example

```bash
python -m packer_builder build -o ~/projects/packer/builds
```
