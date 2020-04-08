from uosatellite.satellite import Satellite

satellite = Satellite("https://satellite.uoregon.edu", username='lcrown', debug=True)

satellite.set_organization("IS")
print("name: {}, id: {}".format(satellite.organization_name, satellite.organization_id))

print("all organizations:")
for org in satellite.organizations:
    print(f"  {org}")
