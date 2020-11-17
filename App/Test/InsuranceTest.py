from App.orm_controllers.DbConnection import DbConnection
from Insurance import Insurance
import pandas as pd
import datetime
import random


def generateRandomDate(startDate: datetime.date, endDate: datetime.date):
    timeBetween = endDate - startDate
    return startDate + datetime.timedelta(days=random.randrange(timeBetween.days))


class InsuranceTest(DbConnection):
    def __init__(self):
        super().__init__()

    def getInsurances(self):
        insurances = self.session.query(Insurance).order_by(Insurance.id)
        print(pd.read_sql_query(insurances.statement, con=self.conn, index_col='id'))

    def deleteAllInsurances(self):
        insurances = self.session.query(Insurance).order_by(Insurance.id)
        for row in insurances:
            self.session.delete(row)
        self.session.commit()

    def addRandomInsurances(self):
        for i in range(1, 20):
            self.session.add(self.__generateRandomInsurance())
        self.session.commit()

    def getMaxId(self):
        insurances = self.session.query(Insurance).order_by(Insurance.id)
        return max(i.id for i in insurances)

    def __generateRandomInsurance(self):
        return Insurance(id=self.getMaxId()+1,\
                         insurer_id=int(random.uniform(1, 10)),\
                         expiration_date=generateRandomDate(datetime.date.fromisoformat("2021-01-01"),\
                                                            datetime.date.fromisoformat("2023-12-12")))



if __name__ == '__main__':
    testInstance = InsuranceTest()
    testInstance.getInsurances()


