import getpass
import json
import os
import requests
import logging

from uosatellite.organization import OrganizationManager
from uosatellite.hosts import HostManager

class Satellite:
    def __init__(self, url, username=None, password=None, debug=False):
        self.debug = debug
        if self.debug:
            logging.basicConfig(level=logging.DEBUG)
            print("\nmuch verbose, so debug, wow\n\n")
        self.logger = logging.getLogger(__name__)
        self.organizations = []
        if not url:
            self.logger.error("You must initialize Satellite with a valid url")
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
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}
        self._login(self.username, self.password)
        self._test_valid_auth()


    def _login(self, username=None, password=None):
        self.logger.debug('setting auth')
        if not username:
            username = input("Enter username: ")
        pw_msg = f"Password for user {username}: "
        if not password:
            password = getpass.getpass(pw_msg)
        self.auth = (username, password)


    def _test_valid_auth(self):
        self.logger.debug('testing valid authentication')
        url = f"{self.url}/api/realms"
        try:
            resp = requests.get(url, auth=self.auth)
            if not resp.ok:
                self.logger.error('Authentication Failed')
                exit(1)
        except requests.exceptions.ConnectionError:
            self.logger.error(f"Failed to connect to server: {self.url}")
            exit(1)



    #----------------------------------#
    #   Public Methods                 #
    #----------------------------------#

    def set_organization(self, name):
        org_mgr = OrganizationManager(self)
        self.organizations = org_mgr.organizations
        org_mgr.set_organization(name)
        self.organization_name = org_mgr.name
        self.organization_id = org_mgr.id
