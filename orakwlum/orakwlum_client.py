# -*- coding: utf-8 -*-

from orakwlum_api import orakWlum_API
import json

# simulate config -> to fetch from real ERP conf
config = {
    'url': 'http://localhost:5000/api/v1',
    'user': "test@gisce.net",
    'password': "test@gisce.net",
}
class orakWlum_client(object):
    def __init__(self):
        self.API = orakWlum_API(**config)

    def consumptions(self, CUPS, date_start, date_end):
        """
        Return consumptions for a CUPS between a range of dates
        """
        return self.API.get(resource="/consumptions")

okW = orakWlum_client()
consumptions = okW.consumptions(CUPS="ES0000000000000000AA", date_start=1472688000, date_end=1475280000)
print (consumptions)
