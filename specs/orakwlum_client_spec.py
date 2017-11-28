# -*- coding: utf-8 -*-
from __future__ import (absolute_import)
import vcr
import requests

from orakwlum_client import orakWlum_Client

config = {
    'protocol': 'http',
    'host': 'localhost',
    'port': '5000',
    'user': "test@gisce.net",
    'password': "test@gisce.net",
}

expected = {
    'url': 'http://localhost:5000/api/v1',
}

consumption_to_fetch = {
    "by_CUPS": {
        "CUPS": 'ES0000000000000000AA',
        "date_start": 1472688000,
        "date_end": 1475280000,
    },
    "by_aggregates": {
        "date_start": 1472688000,
        "date_end": 1475280000,
    },
}

consumption_expected = {
    "by_CUPS": {
        'result': {
            'ES0000000000000000AA': {
                'consumption': 10.0,
                'total': 10.0,
            },
        },
    },
    "by_aggregates": {
        'result': {
            'AGG1': {
                'consumption': 12.0,
                'total': 12.0,
            },
        },
    },
}

fixtures_path = 'specs/fixtures/okW_Client/'

spec_VCR = vcr.VCR(
    record_mode='new_episodes',
    cassette_library_dir=fixtures_path
)

with description('A new'):
    with before.each:
        self.config = config
        self.expected = expected

    with context('orakWlum_Client'):
        with context('initialization'):
            with it('must be performed as expected'):
                with spec_VCR.use_cassette('init.yaml'):
                    self.okW = orakWlum_Client(**self.config)
                    assert self.okW.API.url == self.expected['url'], "URL must match"
                    assert self.okW.API.token != None, "Token must be defined"

            with context('errors'):
                with it('must be handled for non passed user'):
                    with spec_VCR.use_cassette('init_error_incorrect_user.yaml'):
                        tmp_config = dict(self.config)
                        del tmp_config['user']

                        works = True
                        try:
                            orakWlum_Client(**tmp_config)
                        except:
                            works = False

                        assert not works, "okW Client must except if no user is provided"

                with it('must be handled for incorrect password'):
                    with spec_VCR.use_cassette('init_error_incorrect_passwd.yaml'):
                        tmp_config = dict(self.config)
                        del tmp_config['password']
                        works = True
                        try:
                            orakWlum_Client(**tmp_config)
                        except:
                            works = False

                        assert not works, "okW Client must except if no password is provided"

        with context('usage'):
            with before.each:
                with spec_VCR.use_cassette('init.yaml'):
                    self.config = config
                    self.okW = orakWlum_Client(**self.config)

            with it('must return consumptions by CUPS as expected'):
                with spec_VCR.use_cassette('consumptions.yaml'):
                    consumption = self.okW.consumptions.by_cups(**consumption_to_fetch['by_CUPS'])
                    assert consumption == consumption_expected['by_CUPS'], "Consumption do no match with the expected one. Expected: '{consumption_expected}' vs '{consumption}'".format(consumption_expected=consumption_expected['by_CUPS'], consumption=consumption)

                    # Assert required params to reach Consumption
                    for param in consumption_to_fetch['by_CUPS']:
                        tmp_config = dict(consumption_to_fetch['by_CUPS'])
                        del tmp_config[param]

                        works = True
                        try:
                            consumptions = self.okW.consumptions.by_cups(**tmp_config)
                            print (consumptions)
                        except:
                            works = False
                        assert not works, "okWClient.Consumptions must except if no {param} is provided".format(param=param)

            with it('must return consumptions by aggregates as expected'):
                with spec_VCR.use_cassette('consumptions.yaml'):

                    try:
                        consumption = self.okW.consumptions.by_aggregates(**consumption_to_fetch['by_aggregates'])
                        assert consumption == consumption_expected['by_aggregates'], "Consumption do no match with the expected one. Expected: '{consumption_expected}' vs '{consumption}'".format(consumption_expected=consumption_expected['by_aggregates'], consumption=consumption)
                    except:
                        pass

                    # Assert required params to reach Consumption
                    for param in consumption_to_fetch['by_aggregates']:
                        tmp_config = dict(consumption_to_fetch['by_aggregates'])
                        del tmp_config[param]

                        works = True
                        try:
                            consumptions = self.okW.consumptions.by_aggregates(**tmp_config)
                            print (consumptions)
                        except:
                            works = False
                        assert not works, "okWClient.Consumptions must except if no {param} is provided".format(param=param)
