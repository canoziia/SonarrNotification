import re

import sonarrnotification.varparser as varparser


def parse(content: str, escape) -> str:
    return re.sub(r"{{\s*(?P<var>.*?)\s*}}", lambda matched: escape(varparser.get(matched.group("var"))), content, re.DOTALL)
