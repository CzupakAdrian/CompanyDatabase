from database_objects.Objects import Location
from orm_controllers import BaseController
import pandas as pd


# Read only class
class LocationController(BaseController):
    def __init__(self, connection):
        super().__init__(connection)

    def get_all(self):
        return self.session.query(Location)
        # the same as in insurers
        # return pd.read_sql_query(locations.statement, con=self.conn, index_col='id')




