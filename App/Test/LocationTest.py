from App.orm_controllers.DbConnection import DbConnection
from Objects import Location
import pandas as pd
import datetime
import random


class LocationTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getLocations(self):
        locations = self.session.query(Location).order_by(Location.id)
        print(pd.read_sql_query(locations.statement, con=self.conn, index_col='id'))


if __name__ == '__main__':
    testInstance = LocationTest()
    testInstance.getLocations()



