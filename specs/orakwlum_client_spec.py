import vcr
import requests

from orakwlum import orakWlum_Client

config = {
    'url': 'http://localhost:5000/api/v1',
    'user': "test@gisce.net",
    'password': "test@gisce.net",
}

fixtures_path = 'specs/fixtures/okW_Client/'

my_vcr = vcr.VCR(
    record_mode='all',
    cassette_library_dir=fixtures_path
)

with description('A new'):
    with before.each:
        self.config = config

    with context('orakWlum_Client'):
        with context('initialization'):
            with it('must be performed as expected'):
                with my_vcr.use_cassette('init.yaml'):
                    self.okW = orakWlum_Client(**self.config)
                    assert self.okW.API.url == self.config['url'], "URL must match"
                    assert self.okW.API.token != None, "Token must be defined"

            with context('errors'):
                with it('must be handled for non passed user'):
                    with my_vcr.use_cassette('init_error_incorrect_user.yaml'):
                        tmp_config = dict(self.config)
                        del tmp_config['user']

                        works = True
                        try:
                            orakWlum_Client(**tmp_config)
                        except:
                            works = False

                        assert not works, "okW Client must except if no user is provided"

                with it('must be handled for incorrect password'):
                    with my_vcr.use_cassette('init_error_incorrect_passwd.yaml'):
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
                with my_vcr.use_cassette('init.yaml'):
                    self.config = config
                    self.okW = orakWlum_Client(**self.config)

            with it('must return consumptions as expected'):
                with my_vcr.use_cassette('consumptions.yaml'):
                    consumptions = self.okW.consumptions(CUPS="ES0000000000000000AA", date_start=1472688000, date_end=1475280000)
                    print (consumptions)
