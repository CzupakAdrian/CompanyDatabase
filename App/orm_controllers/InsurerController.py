
from orm_controllers.BaseController import BaseController
from database_objects.Objects import Insurer
import pandas as pd


class InsurerController(BaseController):
    def __init__(self, connection):
        super().__init__(connection)

    def get_all(self):
        return self.query(Insurer).order_by(Insurer.id)
        #returning query, cuz boolean conversion
        #   can be interpreted outside like pd.read_sql_query(get_all())
        #return pd.read_sql_query(insurers.statement, con=self.conn, index_col='id')

    def delete_all(self):
        insurers = self.query(Insurer).order_by(Insurer.id)
        for row in insurers:
            self.delete(row)
        self.commit()

    def init(self):
        self.add(Insurer(id=2, name="PZU"))
        self.add(Insurer(id=3, name="XCR"))
        self.add(Insurer(id=4, name="TYIU"))
        self.add(Insurer(id=5, name="PIIK"))
        self.add(Insurer(id=6, name="ADAE"))
        self.add(Insurer(id=7, name="RADAD"))
        self.add(Insurer(id=8, name="ADD"))
        self.add(Insurer(id=9, name="GITI"))
        self.commit()

    def add_insurer(self, name):
        self.add(Insurer(id=1, name=name))
        self.commit()

    def delete_insurer(self, insurer_id):
        insurer = self.query(Insurer).get(insurer_id)
        self.delete(insurer)
        self.commit()


# if __name__ == '__main__':
#     def wait_for_refresh(seconds):
#         print(f'Waiting {seconds}s for refresh ', end='')
#         for i in range(seconds + 1):
#             print('.', end='')
#             time.sleep(1)
#
#     testInstance = InsurerTest()
#     testInstance.add_insurer(12, 'Test insurer')
#     wait_for_refresh(40)
#     testInstance.getInsurers()
#     testInstance.delete_insurer(12)
#     wait_for_refresh(40)
#     testInstance.getInsurers()


