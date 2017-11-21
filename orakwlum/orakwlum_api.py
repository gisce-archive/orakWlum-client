# -*- coding: utf-8 -*-

import requests
import json

AVAILABLE_METHODS = {
    "get": requests.get,
    "post": requests.post,
}

class orakWlum_API(object):
    def __init__(self, url, user, password):
        assert type(url) == str and len(user) > 0 and url.startswith("http"), "Provided URL '{}' is not correct, it must be a string with an URI".format(url)
        assert type(user) == str and len(user) > 0, "Provided user '{}' is not correct, it must be a string".format(user)
        assert type(password) == str and len(password) > 0, "Provided password '{}' is not correct, it must be a string.".format(password)

        self.url = url
        self.token = None

        # Try to login
        self.login(user=user, password=password)

    def API(self, **kwargs):
        """
        Return an API consumer based on the requested method, wrapping requests lib.

        Mandatory params
        - method -> HTTP method to use. Must be activated, see AVAILABLE_METHODS
        - resource -> API resource to consume

        Optional
        - headers
        - data
        - json
        - ... see other abled requests-lib params
        """

        assert "method" in kwargs
        method = kwargs['method']
        assert method in AVAILABLE_METHODS
        del kwargs['method']

        assert "resource" in kwargs
        resource = kwargs['resource']
        assert resource and type(resource) == str, "Resource must be provided as a string"
        assert resource.startswith("/"), "Resource must start with '/'"
        resource = self.url + resource
        del kwargs['resource']

        # Handle incoming headers
        headers = {}
        if "headers" in kwargs and kwargs["headers"]:
            headers = kwargs["headers"]
            assert type(headers) == dict
            del kwargs['headers']

        # Add Authorization header
        if self.token:
            headers['Authorization'] = 'access_token {token}'.format(token=self.token)

        return AVAILABLE_METHODS[method](resource, headers, **kwargs)

    def login(self, user, password):
        """
        Authenticate current client, trying to reach a valid access token.
        """
        login_data = {
            "email": user,
            "password": password,
        }
        r = requests.post(self.url + "/get_token", json=login_data)
        result = r.json()

        # If no error is provided and token is returned assign it
        if ("error" not in result or not result['error']) and "token" in result:
            self.token = result['token']

    def method(self, method, resource, **kwargs):
        """
        Main method handler

        So far, ask the API and return a JSON representation of the response
        """
        result = self.API(method=method, resource=resource, **kwargs)
        return result.json()

    def get(self, resource, **kwargs):
        """
        GET method, it trigger an API.get method consuming the desired resource
        """
        return self.method(method="get", resource=resource, **kwargs)
