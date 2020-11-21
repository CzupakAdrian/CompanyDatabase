from database_objects.Objects import Location
from orm_controllers.BaseController import BaseController
import pandas as pd


def convert_locations_to_pd_dataframe(locations):
    locations_list = [(location.id, location.name) for location in locations]
    return pd.DataFrame(locations_list, columns=['id', 'name'])


# Read only class
class LocationController(BaseController):
    def __init__(self, connection):
        super().__init__(connection)

    def get_all(self):
        return self.query(Location)




