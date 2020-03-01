import getpass
import json
import requests

from satellite.organization import Organization

class Satellite:
    def __init__(self, url=None, username=None, password=None):
        self.organizations = []
        if not url:
            raise ValueError("You must initialize Satellite with a valid url")
        self.url = url
        if username:
            self.username = username
        else:
            self.username = None
        if password:
            self.password = password
        else:
            self.password = None
        self.auth = None
        self._login(self.username, self.password)
        self._get_organizations()

    def _login(self, username=None, password=None):
        if not username:
            username = input("Enter username: ")
        pw_msg = "Password for {}: ".format(username)
        if not password:
            password = getpass.getpass(pw_msg)
        self.auth = (username, password)


    def _get_organizations(self):
        resp = requests.get("{}/katello/api/organizations".format(self.url), auth=self.auth)
        if not resp.ok:
            raise ValueError('Authentication Failed')
        j = json.loads(resp.text)
        for org in j['results']:
            self.organizations.append({'name': org['name'], 'id': org['id']})


    def get_organization(self, name):
        org = Organization(self, name)
        return org
