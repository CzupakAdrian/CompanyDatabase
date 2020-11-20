from orm_controllers.DbConnection import DbConnectionAlbertSarajevo
from database_objects.Objects import GlobalInsurance
import pandas as pd
import datetime
import random


def generateRandomDate(startDate: datetime.date, endDate: datetime.date):
    timeBetween = endDate - startDate
    return startDate + datetime.timedelta(days=random.randrange(timeBetween.days))


class InsuranceGlobalTest:
    def __init__(self, db_connection):
        self.session = db_connection.get_session()
        self.conn = db_connection.get_connection()

    def getInsuranceGlobals(self):
        insurances = self.session.query(GlobalInsurance).order_by(GlobalInsurance.id)
        print(pd.read_sql_query(insurances.statement, con=self.conn, index_col='id'))

    def deleteAllInsuranceGlobals(self):
        insurances = self.session.query(GlobalInsurance).order_by(GlobalInsurance.id)
        for row in insurances:
            self.session.delete(row)
        self.session.commit()

    def addRandomInsuranceGlobals(self):
        for i in range(1, 30):
            self.session.add(self.__generateRandomInsuranceGlobal())
        self.session.commit()

    def getMaxId(self):
        insurances = self.session.query(GlobalInsurance).order_by(GlobalInsurance.id)
        return max(i.id for i in insurances)

    def __generateRandomInsuranceGlobal(self):
        return GlobalInsurance(id=self.getMaxId() + 1,
                               insurer_id=int(random.uniform(1, 9)),
                               expiration_date=generateRandomDate(datetime.date.fromisoformat("2021-01-01"),
                                                                  datetime.date.fromisoformat("2023-12-12")))

    def add_insurance(self, insurance_id, insurer_id, expiration_date: datetime.date):
        self.session.add(GlobalInsurance(id=insurance_id,
                                         insurer_id=insurer_id,
                                         expiration_date=expiration_date))
        self.session.commit()

    def delete_insurance(self, insurance_id):
        insurance = self.session.query(GlobalInsurance).get(insurance_id)
        self.session.delete(insurance)
        self.session.commit()


# init insurances after init insurers
if __name__ == '__main__':
    testInstance = InsuranceGlobalTest(DbConnectionAlbertSarajevo())
    testInstance.getInsuranceGlobals()
    # testInstance.add_insurance(1, 1, datetime.date(2031, 1, 21))
    # testInstance.getInsuranceGlobals()
    # testInstance.delete_insurance(11)
    # testInstance.getInsuranceGlobals()
