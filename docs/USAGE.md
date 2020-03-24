# Packer Builder Usage

## Help

```bash
python -m packer_builder --help
...
usage: __main__.py [-h] [-d DISTRO] [-b BUILDER] [-f FILE] [-n NUMDAYS]
                   [-o OUTPUTDIR] [-p PASSWORD]
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
  -p PASSWORD, --password PASSWORD
                        Define default password to override distros.yml
```

## Examples

### Build All Distros For All Builders

This will build all distros for all builders.

```bash
python -m packer_builder build -o ~/projects/packer/builds
```

### Build All Distros For A Specific Builder

This will build all distros for a specific builder (virtualbox-iso in this
example).

```bash
python -m packer_builder build -o ~/projects/packer/builds -b virtualbox-iso
```

### Build A Specific Distro For All Builders

This will build a specific distro (CentOS in this example) for all builders.

```bash
python -m packer_builder build -o ~/projects/packer/builds -d CentOS
```

### Build A Specific Distro For A Specific Builder

This will build a specific distro (CentOS in this example) for a specific
builder (virtualbox-iso in this example).

```bash
python -m packer_builder build -o ~/projects/packer/builds -d CentOS -b virtualbox-iso
```

### Define Default Password At Runtime

Because there might be a scenario in which you would want to override the password
for all distros defined in `distros.yml`. You can pass this override password as
part of the CLI arguments.

```bash
python -m packer_builder build -o ~/projects/packer/builds -p SuperSecretPass
```

### Generate Templates (ONLY)

```bash
python -m packer_builder generate-templates --outputdir ~/projects/packer
```

## vagrant-libvirt plugin on macOS

```bash
brew install libiconv gcc libvirt
```

```bash
RV=$(/opt/vagrant/embedded/bin/ruby --version | awk '{ print $2 }'| awk '{ split($0, a, "p"); print a[1] }')
CONFIGURE_ARGS='with-ldflags=-L/opt/vagrant/embedded/lib with-libvirt-include=/usr/local/include/libvirt with-libvirt-lib=/usr/local/lib' \
GEM_HOME=~/.vagrant.d/gems/$RV \
GEM_PATH=$GEM_HOME:/opt/vagrant/embedded/gems \
PATH=/opt/vagrant/embedded/bin:$PATH \
vagrant plugin install vagrant-libvirt
```
