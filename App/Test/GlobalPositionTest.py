from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import GlobalPosition
import pandas as pd


class GlobalPositionTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getPositions(self):
        positions = self.session.query(GlobalPosition).order_by(GlobalPosition.position)
        print(pd.read_sql_query(positions.statement, con=self.conn))

    # def deleteAllPositions(self):
    #     positions = self.session.query(Position).order_by(Position.id)
    #     for row in positions:
    #         self.session.delete(row)
    #     self.session.commit()

    def add_position(self, name):
        self.session.add(GlobalPosition(position=name))
        self.session.commit()

    def delete_positon(self, name):
        position = self.session.query(GlobalPosition).get(name)
        self.session.delete(position)
        self.session.commit()


if __name__ == '__main__':
    testInstance = GlobalPositionTest()
    testInstance.add_position('Test')
    testInstance.getPositions()
    testInstance.delete_positon('Test')
    testInstance.getPositions()


