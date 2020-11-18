from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import GlobalInsurance
import pandas as pd
import datetime
import random


def generateRandomDate(startDate: datetime.date, endDate: datetime.date):
    timeBetween = endDate - startDate
    return startDate + datetime.timedelta(days=random.randrange(timeBetween.days))


class InsuranceGlobalTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getInsuranceGlobals(self):
        insurances = self.session.query(GlobalInsurance).order_by(GlobalInsurance.id)
        print(pd.read_sql_query(insurances.statement, con=self.conn, index_col='id'))

    def deleteAllInsuranceGlobals(self):
        insurances = self.session.query(GlobalInsurance).order_by(GlobalInsurance.id)
        for row in insurances:
            self.session.delete(row)
        self.session.commit()

    def addRandomInsuranceGlobals(self):
        for i in range(1, 20):
            self.session.add(self.__generateRandomInsuranceGlobal())
        self.session.commit()

    def getMaxId(self):
        insurances = self.session.query(GlobalInsurance).order_by(GlobalInsurance.id)
        return max(i.id for i in insurances)

    def __generateRandomInsuranceGlobal(self):
        return GlobalInsurance(id=self.getMaxId() + 1,
                               insurer_id=int(random.uniform(1, 10)),
                               expiration_date=generateRandomDate(datetime.date.fromisoformat("2021-01-01"),
                                                                  datetime.date.fromisoformat("2023-12-12")))


if __name__ == '__main__':
    testInstance = InsuranceGlobalTest()
    testInstance.getInsuranceGlobals()
