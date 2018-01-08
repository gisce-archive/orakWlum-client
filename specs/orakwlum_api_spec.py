# -*- coding: utf-8 -*-
from __future__ import (absolute_import)
import vcr
import requests

from orakwlum_client import orakWlum_API

config = {
    'url': 'http://localhost:5000',
    'user': "test@gisce.net",
    'password': "test@gisce.net",
}

expected = {
    'url': 'http://localhost:5000/api/v1',
}

fixtures_path = 'specs/fixtures/okW_API/'

spec_VCR = vcr.VCR(
    record_mode='new_episodes',
    cassette_library_dir=fixtures_path
)

with description('A new'):
    with before.each:
        self.config = config
        self.expected = expected

    with context('orakWlum_API'):
        with context('initialization'):
            with it('must be performed as expected'):
                with spec_VCR.use_cassette('login.yaml'):
                    self.API = orakWlum_API(**self.config)
                    assert self.API.url == self.expected['url'], "URL must match"
                    #assert self.API.token != None, "Token must be defined"

            with context('errors'):
                with it('must be handled for incorrect user'):
                    with spec_VCR.use_cassette('error_login_incorrect_user.yaml'):
                        self.config['user'] = "non-existent-user"
                        self.API = orakWlum_API(**self.config)
                        assert self.API.url == self.expected['url'], "URL must match"
                        #assert self.API.token == None, "Token must not be defined for erroneous login"

                with it('must be handled for incorrect password'):
                    with spec_VCR.use_cassette('error_login_incorrect_passwd.yaml'):
                        self.config['password'] = "incorrect-password"
                        self.API = orakWlum_API(**self.config)
                        assert self.API.url == self.expected['url'], "URL must match"
                        #assert self.API.token == None, "Token must not be defined for erroneous login"


        with context('usage'):
            with before.each:
                with spec_VCR.use_cassette('login.yaml'):
                    self.config = config
                    self.API = orakWlum_API(**self.config)

            with it('must be performed as expected for GET requests'):
                with spec_VCR.use_cassette('get.yaml'):
                    self.API.get("/")
                    assert self.API.token == None, "Token must not be defined for erroneous login"

            with it('must be performed as expected for GET requests with own headers'):
                with spec_VCR.use_cassette('get.yaml'):
                    own_headers = {'rolf': 'me'}
                    self.API.get("/", headers=own_headers)
                    assert self.API.token == None, "Token must not be defined for erroneous login"
