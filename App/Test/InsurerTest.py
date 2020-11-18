from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import Insurer
import pandas as pd


class InsurerTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getInsurers(self):
        insurers = self.session.query(InsurerLocal).order_by(InsurerLocal.id)
        print(pd.read_sql_query(insurers.statement, con=self.conn, index_col='id'))

    def deleteAllInsurers(self):
        insurers = self.session.query(InsurerLocal).order_by(InsurerLocal.id)
        for row in insurers:
            self.session.delete(row)
        self.session.commit()

    # Won't work with self.getMaxInsurerId() from Sarajevo because id error (refresh time takes 10s to uptadte it locally)
    def addInsurers(self):
        self.session.add(Insurer(id=2, name="AXA"))
        self.session.add(Insurer(id=3, name="PZU"))
        self.session.add(Insurer(id=4, name="XCR"))
        self.session.add(Insurer(id=5, name="TYIU"))
        self.session.add(Insurer(id=6, name="PIIK"))
        self.session.add(Insurer(id=7, name="ADAE"))
        self.session.add(Insurer(id=8, name="RADAD"))
        self.session.add(Insurer(id=9, name="ADD"))
        self.session.add(Insurer(id=10, name="GITI"))
        self.session.commit()

    def getMaxInsurerId(self):
        insurers = self.session.query(InsurerLocal).order_by(InsurerLocal.id)
        return max(i.id for i in insurers)


if __name__ == '__main__':
    testInstance = InsurerTest()
    # testInstance.session.add(Insurer(id=2, name="ALLA"))
    # testInstance.session.commit()
    # testInstance.addInsurers()
    testInstance.getInsurers()


