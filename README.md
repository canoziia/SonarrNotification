# SonarrNotification

a Sonarr custom script to send notifications

## Getting Started

-   [Usage](#usage)
-   [Build](#build)
-   [Download](https://github.com/canoziia/SonarrNotification/releases)

## Usage

### Install

```bash
$ git clone https://github.com/canoziia/SonarrNotification.git
$ cd SonarrNotification
$ python setup.py install
```

### Command

```bash
$ snotif --help
Usage: snotif [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  send

$ snotif send --help
Sonarr custom notification scripts
Usage: snotif send [OPTIONS]

Options:
  -c, --config FILE
  --help             Show this message and exit.
```

### Config

[config_example.yaml](config.yaml)

### Notification Template

If template is not set in the configuration file, it will use the built-in [template](template).

Python code/functions can be used in template files, just use double curly braces outside:

Python code

```
{{ print("Hello World") }}
```

Built-in function

```
{{ series_image }}
```

or custom functions in [custom](custom)

```
{{ download_type }}
```

It can also use environment variables offered by [Sonarr](https://wiki.servarr.com/sonarr/custom-scripts#environment-variables) or others like this:

```
{{ $sonarr_series_tvmazeid$ }}
```

### Set in Sonarr

create a shell script (send.sh)

```bash
#!/bin/bash
# export HTTP_PROXY=http://127.0.0.1:7890
# export HTTPS_PROXY=http://127.0.0.1:7890
logsave -a logs.txt snotif send -c config.yaml
```

![set in sonarr](docs/assets/images/set%20in%20sonarr.png)

## Build

Use pyinstaller to package this script as an executable:

```bash
$ sudo apt install virtualenv -y
$ virtualenv ~/pyenv && source ~/pyenv/bin/activate
$ pip install pyinstaller
$ python setup install
$ pyinstaller snotif.spec
$ cp dist/snotif /path/you/need
```

or download from [Releases](https://github.com/canoziia/SonarrNotification/releases)
