from App.orm_controllers.DbConnection import DbConnection
from Objects import Insurer
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
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="AXA"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="PZU"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="XCR"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="TYIU"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="PIIK"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="ADAE"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="RADAD"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="ADD"))
        self.session.add(Insurer(id=self.getMaxInsurerId() + 1, name="GITI"))
        self.session.commit()

    def getMaxInsurerId(self):
        insurers = self.session.query(Insurer).order_by(Insurer.id)
        return max(i.id for i in insurers)



if __name__ == '__main__':
    testInstance = InsurerTest()
    testInstance.session.add(Insurer(id=1, name="ALLA"))
    testInstance.session.commit()
    testInstance.addInsurers()
    testInstance.getInsurers()


