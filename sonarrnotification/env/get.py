import os


def get(name: str) -> str:
    if name in os.environ:
        return os.environ[name]
    else:
        return None
