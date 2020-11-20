from orm_controllers.DbConnection import DbConnectionAlbertSarajevo
from database_objects.Objects import GlobalPosition
import pandas as pd


class GlobalPositionTest:
    def __init__(self, db_connection):
        self.session = db_connection.get_session()
        self.conn = db_connection.get_connection()

    def get_positions(self):
        positions = self.session.query(GlobalPosition).order_by(GlobalPosition.position)
        return pd.read_sql_query(positions.statement, con=self.conn)

    # def deleteAllPositions(self):
    #     positions = self.session.query(Position).order_by(Position.id)
    #     for row in positions:
    #         self.session.delete(row)
    #     self.session.commit()

    def add_position(self, name):
        self.session.add(GlobalPosition(position=name))
        self.session.commit()

    def delete_position(self, name):
        position = self.session.query(GlobalPosition).get(name)
        self.session.delete(position)
        self.session.commit()


if __name__ == '__main__':
    testInstance = GlobalPositionTest(DbConnectionAlbertSarajevo())
    # testInstance.add_position('Test')
    print(testInstance.get_positions())
    # testInstance.delete_position('Test')
    # print(testInstance.get_positions())


