# -*- coding: utf-8 -*-

from orakwlum_api import orakWlum_API
import json

class orakWlum_Client(object):
    def __init__(self, **config):
        self.API = orakWlum_API(**config)

    def consumptions(self, CUPS, date_start, date_end):
        """
        Return consumptions for a CUPS between a range of dates
        """
        return self.API.get(resource="/consumptions")
