from orm_controllers.BaseController import BaseController
from database_objects.Objects import GlobalPosition
import pandas as pd

from orm_controllers.DbConnection import DbConnectionAlbertSarajevo, DbConnectionAdrianSarajevo


def convert_positions_to_pd_dataframe(positions):
    positions_list = [position.position for position in positions]
    return pd.DataFrame(positions_list, columns=['position'])

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
    testInstance = GlobalPositionController(DbConnectionAdrianSarajevo())
    # testInstance.add_position('Test')
    positions = convert_positions_to_pd_dataframe(testInstance.get_all())
    print(positions.to_string())
    testInstance.delete("Waiter")
    # testInstance.delete_position('Test')
    # testInstance.getPositions()
