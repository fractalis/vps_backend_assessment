from .swapi.client import SWAPIClient

import locale

class VPSBackendAssessment(object):

    @staticmethod
    def run():
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        client = SWAPIClient()
        starship_collection = client.fetch_starships()

        for item in starship_collection.iter():
            print(f'Ship Name: {item.name}')
            if(len(item.pilots) > 0):
                print(f'\tPilots:')
                for pilot in item.fetch_pilots():
                    print(f'\t\t{pilot.name}')

        
    