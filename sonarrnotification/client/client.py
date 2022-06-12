import os
import sys
import requests
import html

import sonarrnotification.varparser as varparser

exts = {"MarkdownV2": "md", "HTML": "html", "Markdown": "md"}


def mainexec_dir():
    if getattr(sys, 'frozen', False):
        # is Bundle Resource
        return sys._MEIPASS
    else:
        # os.path.abspath(sys.argv[0])
        return os.path.abspath(".")


def parseSender(config):
    if config["type"] == "telegram":
        return telegram(config)


class telegram:
    def __init__(self, config):
        self.token = str(config["token"])
        self.chat_id = config["chat_id"]
        self.parse_mode = str(config["parse_mode"])
        self.disable_web_page_preview = config["disable_web_page_preview"]
        self.disable_notification = config["disable_notification"]
        self.protect_content = config["protect_content"]
        if (not "template" in config) or config["template"] == None:
            # use build-in template
            self.template = os.path.join(
                mainexec_dir(), f"template/{self.parse_mode}")
        else:
            # use external template
            self.template = str(config["template"]) if os.path.isabs(
                str(config["template"])) else os.path.join(os.path.abspath("."), str(config["template"]))
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.text = {}

    def escape(self, text: str) -> str:
        if self.parse_mode == "HTML":
            return html.escape(text)
        elif self.parse_mode == "Markdown":
            # warning: markdown support is still under development
            return text
        elif self.parse_mode == "MarkdownV2":
            # warning: markdown support is still under development
            return text
        else:
            # impossible
            pass

    def send(self, chat_id, eventtype):
        if not eventtype in self.text:
            self.text[eventtype] = varparser.parse(
                open(os.path.join(self.template,
                     f"{eventtype}.{exts[self.parse_mode]}")).read(),
                # open(os.path.join(self.template, eventtype)).read(),
                self.escape
            )
        text = self.text[eventtype]
        message = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": self.parse_mode,
            "disable_web_page_preview": self.disable_web_page_preview,
            "disable_notification": self.disable_notification,
            "protect_content": self.protect_content,
        }
        resp = requests.post(f"{self.url}/sendMessage", json=message)
        if resp.status_code == 200:
            print(f"successfully send message to {chat_id}")
        else:
            print(f"failed to send message to {chat_id}: {resp.text}")

    def sendAll(self, eventtype):
        for chat_id in self.chat_id:
            self.send(chat_id, eventtype)


class client:
    def __init__(self, config):
        self.notification = config["notification"]
        self.sender = {}
        for senderName in self.notification:
            self.sender[senderName] = parseSender(config[senderName])

    def send(self, senderName, eventtype):
        self.sender[senderName].sendAll(eventtype)

    def sendAll(self, eventtype):
        for sender in self.sender.keys():
            self.send(sender, eventtype)
