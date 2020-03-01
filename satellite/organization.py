class Organization:
    def __init__(self, satellite, name):
        self.name = None
        self.id = None
        for org in satellite.organizations:
            if org['name'] == name:
                self.name = name
                self.id = org['id']
        if self.name == None or self.id == None:
            raise ValueError('Organization Not Found')
