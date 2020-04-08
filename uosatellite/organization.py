import json
import logging
import requests

class OrganizationManager:
    def __init__(self, satellite):
        self.name = None
        self.id = None

        self.satellite = satellite

        if self.satellite.debug:
            logging.basicConfig(level=logging.DEBUG)
            print("\nmuch verbose, so debug, wow\n\n")
        self.logger = logging.getLogger(__name__)

        self.organizations = []
        self._get_organizations()

    def _get_organizations(self):
        self.logger.debug('getting all organizations')
        url = f"{self.satellite.url}/katello/api/organizations"
        resp = requests.get(url, auth=self.satellite.auth)
        j = json.loads(resp.text)
        for org in j['results']:
            self.organizations.append({'name': org['name'], 'id': org['id']})

    def set_organization(self, name):
        self.logger.debug('setting organization')
        for org in self.organizations:
            if org['name'] == name:
                self.name = name
                self.id = org['id']
        if self.name == None or self.id == None:
            raise ValueError('Organization Not Found')
