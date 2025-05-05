#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "22467463"))
    API_HASH = os.environ.get("API_HASH", "156c0c4ecf6c03b4eb4ea9ac36e465d0")
    AUTH_USERS = "1621539522"
    LOG_CHAT_ID = int(os.environ.get("LOG_CHAT_ID", "-1002501498543"))

