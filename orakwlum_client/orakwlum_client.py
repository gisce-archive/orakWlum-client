# -*- coding: utf-8 -*-
from .orakwlum_api import orakWlum_API
from .consumptions import Consumptions

class orakWlum_Client(object):
    def __init__(self, **config):
        """
        Initializes an orakWlum client

        Mandatory params:
        - host
        - port
        - user
        - password

        Optional:
        - protocol: "http" or "https"
        """
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

        # Prepare consumptions method
        self.consumptions = Consumptions(self.API)
