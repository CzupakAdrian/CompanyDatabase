from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import Location
import pandas as pd

#Read only class
class LocationTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getLocation(self):
        locations = self.session.query(Location)
        return pd.read_sql_query(locations.statement, con=self.conn, index_col='id')


if __name__ == '__main__':
    testInstance = LocationTest()
    print(testInstance.getLocation())



