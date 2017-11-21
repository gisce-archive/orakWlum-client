# -*- coding: utf-8 -*-
from .orakwlum_api import orakWlum_API
import json

class orakWlum_Client(object):
    def __init__(self, **config):
        assert "host" in config
        assert "port" in config
        assert "user" in config
        assert "password" in config

        # Set protocol to https by default
        protocol = "https"
        if "protocol" in config:
            protocol = config['protocol']

        url = "{protocol}://{host}:{port}".format(protocol=protocol, host=config["host"], port=config["port"])
        config = {
            "url": url,
            "user": config['user'],
            "password": config['password'],
        }
        self.API = orakWlum_API(**config)

    def consumptions(self, CUPS, date_start, date_end):
        """
        Return consumptions for a CUPS between a range of dates
        """
        params = {
            "date_start": date_start,
            "date_end": date_end,
        }
        return self.API.get(resource="/consumptions/" + CUPS, params=params)
