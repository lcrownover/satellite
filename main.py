import requests

from satellite import satellite

satellite = satellite.Satellite("https://satellite.uoregon.edu", 'lcrown')

organization = satellite.get_organization("IS")
print("name: {}, id: {}".format(organization.name, organization.id))
