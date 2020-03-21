# packer-builder

Using Packer **SHOULD** be straight forward and in most cases, it is. Packer builder abstracts many of the complexities of building images. With Packer builder, we wrap many of these complexities within code. By doing this, it provides us with a consistent model to build our images. We can inject logic which many times is not apparent. In addition to all of this, implement best practices into our builds. Is this builder for everyone? No. But for many, Packer can be a daunting process. So, we can minimize these processes, and make Packer builds more consumable.

## Build Status

### GitHub Actions

![Python Test](https://github.com/mrlesmithjr/packer-builder/workflows/Python%20Test/badge.svg)

### Travis CI

[![Build Status](https://travis-ci.org/mrlesmithjr/packer-builder.svg?branch=master)](https://travis-ci.org/mrlesmithjr/packer-builder)

## Usage

### Help

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

### Examples

#### Build All Distros For All Builders

This will build all distros for all builders.

```bash
python -m packer_builder build -o ~/projects/packer/builds
```

#### Build All Distros For A Specific Builder

This will build all distros for a specific builder (virtualbox-iso in this
example).

```bash
python -m packer_builder build -o ~/projects/packer/builds -b virtualbox-iso
```

#### Build A Specific Distro For All Builders

This will build a specific distro (CentOS in this example) for all builders.

```bash
python -m packer_builder build -o ~/projects/packer/builds -d CentOS
```

#### Build A Specific Distro For A Specific Builder

This will build a specific distro (CentOS in this example) for a specific
builder (virtualbox-iso in this example).

```bash
python -m packer_builder build -o ~/projects/packer/builds -d CentOS -b virtualbox-iso
```

#### Define Default Password At Runtime

Because there might be a scenario in which you would want to override the password
for all distros defined in `distros.yml`. You can pass this override password as
part of the CLI arguments.

```bash
python -m packer_builder build -o ~/projects/packer/builds -p SuperSecretPass
```

#### Generate Templates (ONLY)

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

## Requirements

- [requirements.txt](requirements.txt)
- [requirements-dev.txt](requirements-dev.txt)

## Dependencies

## Documentation

Checkout [https://mrlesmithjr.github.io/packer-builder](https://mrlesmithjr.github.io/packer-builder) for project documentation.

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
- [http://everythingshouldbevirtual.com](http://everythingshouldbevirtual.com)

> NOTE: Repo has been created/updated using [https://github.com/mrlesmithjr/cookiecutter-python-project](https://github.com/mrlesmithjr/cookiecutter-python-project) as a template.
