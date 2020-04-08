import json
import logging
import requests

class HostManager:
    def __init__(self, satellite):
        self.satellite = satellite

        if self.satellite.debug:
            logging.basicConfig(level=logging.DEBUG)
            print("\nmuch verbose, so debug, wow\n\n")
        self.logger = logging.getLogger(__name__)
