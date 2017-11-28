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

    def consumptions_by_cups (self, CUPS, date_start, date_end):
        """
        Return consumptions for a CUPS (or a list) between a range of dates

        - dates must be timestamps
        - CUPS can be a string or a list of strings with the CUPS
        """
        params = {
            "date_start": date_start,
            "date_end": date_end,
            "cups": CUPS,
        }
        return self.API.get(resource="/consumptions", params=params)

    def consumptions_by_aggregates (self, date_start, date_end, aggregates=None):
        """
        Return consumptions grouped by REE aggregates between a range of dates

        - dates must be timestamps
        - aggregates can be the list of aggregates to reach or None
        """
        params = {
            "date_start": date_start,
            "date_end": date_end,
        }
        return self.API.get(resource="/consumptions_by_aggregates", params=params)
