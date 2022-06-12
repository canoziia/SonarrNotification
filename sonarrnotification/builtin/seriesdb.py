import requests
import sonarrnotification.env as env


tvmaze_url = "https://api.tvmaze.com"


def series_json():
    tvmazeid = env.get("sonarr_series_tvmazeid")
    resp = requests.get(f"{tvmaze_url}/shows/{tvmazeid}")
    if resp.status_code != 200:
        return {}
    else:
        return resp.json()


def series_url() -> str:
    return series_json()["url"]


def series_image() -> str:
    js = series_json()
    if js["image"] == None:
        # return series url
        return js["url"]
    else:
        return js["image"]["original"]


def episode_json(episode_inner_id):
    # sonarr_episodefile_episodenumbers contains multiple episodes
    tvmazeid = env.get("sonarr_series_tvmazeid")
    season = env.get("sonarr_episodefile_seasonnumber")
    resp = requests.get(
        f"{tvmaze_url}/shows/{tvmazeid}/episodebynumber?season={season}&number={episode_inner_id}")
    if resp.status_code != 200:
        return {}
    else:
        return resp.json()


def seasons_json():
    tvmazeid = env.get("sonarr_series_tvmazeid")
    resp = requests.get(f"{tvmaze_url}/shows/{tvmazeid}/seasons")
    return resp.json()


def episode_url() -> str:
    episode_inner_id = env.get("sonarr_episodefile_id")  # only first one
    return episode_json(episode_inner_id)["url"]


def episode_image() -> str:
    episode_inner_id = env.get("sonarr_episodefile_id")  # only first one
    js = episode_json(episode_inner_id)
    if js["image"] == None:
        # return episode url
        return js["url"]
    else:
        return js["image"]["original"]
