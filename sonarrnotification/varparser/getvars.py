import re

import sonarrnotification.env as env
from sonarrnotification.builtin import *
from sonarrnotification.custom import *


def get(content: str) -> str:
    # str, code, func, func()
    c = re.sub(r"\$(?P<env>\w*?)\$",
               lambda matched: str(env.get(matched.group("env"))), content)
    try:
        # code, func, func()
        t = eval(c)
        if callable(t):
            # func
            res = t()
        else:
            # code, func()
            res = t
    except:
        # str
        res = c
    return str(res)
