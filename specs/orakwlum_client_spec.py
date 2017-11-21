import vcr
import requests

from orakwlum import orakWlum_Client

config = {
    'url': 'http://localhost:5000/api/v1',
    'user': "test@gisce.net",
    'password': "test@gisce.net",
}

fixtures_path = 'specs/fixtures/okW_Client/'

with description('A new'):
    with before.each:
        self.config = config

    with context('orakWlum_Client'):
        with context('initialization'):
            with it('must be performed as expected'):
                with vcr.use_cassette(fixtures_path + 'init.yaml'):
                    self.okW = orakWlum_Client(**self.config)
                    assert self.okW.API.url == self.config['url'], "URL must match"
                    assert self.okW.API.token != None, "Token must be defined"

            with context('errors'):
                with it('must be handled for incorrect user'):
                    with vcr.use_cassette(fixtures_path + 'init_error_incorrect_user.yaml'):
                        self.config['user'] = "non-existent-user"
                        self.okW = orakWlum_Client(**self.config)
                        assert self.okW.API.token == None, "Token must not be defined for erroneous login"

                with it('must be handled for incorrect password'):
                    with vcr.use_cassette(fixtures_path + 'init_error_incorrect_passwd.yaml'):
                        self.config['password'] = "incorrect-password"
                        self.okW = orakWlum_Client(**self.config)
                        assert self.okW.API.token == None, "Token must not be defined for erroneous login"

        with context('usage'):
            with before.each:
                with vcr.use_cassette(fixtures_path + 'init.yaml'):
                    self.config = config
                    self.okW = orakWlum_Client(**self.config)

            with it('must return consumptions as expected'):
                with vcr.use_cassette(fixtures_path + 'consumptions.yaml'):
                    consumptions = self.okW.consumptions(CUPS="ES0000000000000000AA", date_start=1472688000, date_end=1475280000)
                    print (consumptions)
