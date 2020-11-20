import time

from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import Insurer
import pandas as pd


class InsurerTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getInsurers(self):
        insurers = self.session.query(Insurer).order_by(Insurer.id)
        print(pd.read_sql_query(insurers.statement, con=self.conn, index_col='id'))

    def deleteAllInsurers(self):
        insurers = self.session.query(Insurer).order_by(Insurer.id)
        for row in insurers:
            self.session.delete(row)
        self.session.commit()

    def addInsurers(self):
        self.session.add(Insurer(id=2, name="PZU"))
        self.session.add(Insurer(id=3, name="XCR"))
        self.session.add(Insurer(id=4, name="TYIU"))
        self.session.add(Insurer(id=5, name="PIIK"))
        self.session.add(Insurer(id=6, name="ADAE"))
        self.session.add(Insurer(id=7, name="RADAD"))
        self.session.add(Insurer(id=8, name="ADD"))
        self.session.add(Insurer(id=9, name="GITI"))
        self.session.commit()

    def add_insurer(self, insurer_id, name):
        self.session.add(Insurer(id=insurer_id, name=name))
        self.session.commit()

    def delete_insurer(self, insurer_id):
        insurer = self.session.query(Insurer).get(insurer_id)
        self.session.delete(insurer)
        self.session.commit()


if __name__ == '__main__':
    def wait_for_refresh(seconds):
        print(f'Waiting {seconds}s for refresh ', end='')
        for i in range(seconds + 1):
            print('.', end='')
            time.sleep(1)

    testInstance = InsurerTest()
    testInstance.add_insurer(12, 'Test insurer')
    wait_for_refresh(40)
    testInstance.getInsurers()
    testInstance.delete_insurer(12)
    wait_for_refresh(40)
    testInstance.getInsurers()


