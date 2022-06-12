import sonarrnotification.client as client


def send(config, sonarr_eventtype):
    instance = client.client(config)
    instance.sendAll(sonarr_eventtype)
