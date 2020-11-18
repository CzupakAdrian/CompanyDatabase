from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import Position
import pandas as pd


class PositionTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getPositions(self):
        positions = self.session.query(Position).order_by(Position.id)
        print(pd.read_sql_query(positions.statement, con=self.conn, index_col='id'))

    def deleteAllPositions(self):
        positions = self.session.query(Position).order_by(Position.id)
        for row in positions:
            self.session.delete(row)
        self.session.commit()


    def addPositions(self):
        self.session.add(Position(id=1, position="Kierownik"))
        self.session.add(Position(id=2, position="Stażysta"))
        self.session.add(Position(id=3, position="HR"))
        self.session.add(Position(id=4, position="Tester"))
        self.session.add(Position(id=5, position="Sprzątacz"))
        self.session.add(Position(id=6, position="Stołówkowa"))
        self.session.add(Position(id=7, position="Scrum Master"))
        self.session.commit()


if __name__ == '__main__':
    testInstance = PositionTest()
    testInstance.getPositions()
    # testInstance.addPositions()
    testInstance.getPositions()


