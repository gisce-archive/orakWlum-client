import vcr
import requests

from orakwlum import orakWlum_API

config = {
    'url': 'http://localhost:5000/api/v1',
    'user': "test@gisce.net",
    'password': "test@gisce.net",
}

fixtures_path = 'specs/fixtures/'

with description('A new'):
    with before.each:
        self.config = config

    with context('orakWlum_API'):
        with context('initialization'):
            with it('must be performed as expected'):
                with vcr.use_cassette(fixtures_path + 'okW_API_login.yaml'):
                    self.API = orakWlum_API(**self.config)
                    assert self.API.url == self.config['url'], "URL must match"
                    assert self.API.token != None, "Token must be defined"

            with context('errors'):
                with it('must be handled for incorrect user'):
                    with vcr.use_cassette(fixtures_path + 'okW_API_error_login_incorrect_user.yaml'):
                        self.config['user'] = "non-existent-user"
                        self.API = orakWlum_API(**self.config)
                        assert self.API.url == self.config['url'], "URL must match"
                        assert self.API.token == None, "Token must not be defined for erroneous login"

                with it('must be handled for incorrect password'):
                    with vcr.use_cassette(fixtures_path + 'okW_API_error_login_incorrect_passwd.yaml'):
                        self.config['password'] = "incorrect-password"
                        self.API = orakWlum_API(**self.config)
                        assert self.API.url == self.config['url'], "URL must match"
                        assert self.API.token == None, "Token must not be defined for erroneous login"

        with context('consumption'):
            with before.each:
                with vcr.use_cassette(fixtures_path + 'okW_API_login.yaml'):
                    self.config = config
                    self.API = orakWlum_API(**self.config)

            with it('must be performed as expected for GET requests'):
                with vcr.use_cassette(fixtures_path + 'okW_API_get.yaml'):
                    pass
