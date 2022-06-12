import sonarrnotification.env as env


def download_type() -> str:
    if env.get("sonarr_isupgrade") == "True":
        # Upgrade
        return "升级"
    else:
        # Import
        return "导入"
