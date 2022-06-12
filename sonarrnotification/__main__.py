import yaml
import click

import sonarrnotification.env as env
import sonarrnotification.commands as commands

__version__ = "0.0.1"
__description__ = "Sonarr custom notification scripts"


@click.version_option(prog_name="Sonarr Notification", version=__version__)
@click.group()
def main():
    click.echo(__description__)


@main.command()
@click.option(
    "--config", "-c",
    type=click.Path(exists=True, resolve_path=True,
                    file_okay=True, dir_okay=False), default="config.yaml"
)
def send(config):
    sonarr_eventtype = env.get("sonarr_eventtype")
    configObj = yaml.safe_load(open(config).read())
    commands.send(configObj, sonarr_eventtype)


if __name__ == "__main__":
    main()
