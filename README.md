# packer-builder

## Usage

### Help

```bash
python -m packer_builder --help
...
usage: __main__.py [-h] -f FILE -o OUTPUTDIR

Packer template builder.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to distro
  -o OUTPUTDIR, --outputdir OUTPUTDIR
```

### Example

```bash
python -m packer_builder -o ~/projects/packer/builds
```
