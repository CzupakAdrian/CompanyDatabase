from orm_controllers.BaseController import BaseController
from database_objects.Objects import GlobalPosition
import pandas as pd


class GlobalPositionController(BaseController):
    def __init__(self, controller):
        super().__init__(controller)

    def get_all(self):
        return self.query(GlobalPosition).order_by(GlobalPosition.position)
        #return pd.read_sql_query(positions.statement, con=self.conn)

    # def deleteAllPositions(self):
    #     positions = self.session.query(Position).order_by(Position.id)
    #     for row in positions:
    #         self.session.delete(row)
    #     self.session.commit()

    def add_position(self, name):
        self.add(GlobalPosition(position=name))
        self.commit()

    def delete_position(self, name):
        position = self.query(GlobalPosition).get(name)
        self.delete(position)
        self.commit()


if __name__ == '__main__':
    testInstance = GlobalPositionController()
    testInstance.add_position('Test')
    testInstance.getPositions()
    testInstance.delete_position('Test')
    testInstance.getPositions()
