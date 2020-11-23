from orm_controllers.BaseController import BaseController
from database_objects.Objects import GlobalInsurance
import pandas as pd
import datetime
import random


def generate_random_date(startDate: datetime.date, endDate: datetime.date):
    timeBetween = endDate - startDate
    return startDate + datetime.timedelta(days=random.randrange(timeBetween.days))


def convert_insurances_to_pd_dataframe(insurances):
    locations_list = [(insurance.id, insurance.expiration_date, insurance.insurer.name) for insurance in insurances]
    return pd.DataFrame(locations_list, columns=['id', 'expiration date', 'insurer'])

class InsuranceController(BaseController):
    def __init__(self, connection):
        super().__init__(connection)

    def get_all(self):
        return self.query(GlobalInsurance).order_by(GlobalInsurance.id)
        #return pd.read_sql_query(insurances.statement, con=self.conn, index_col='id')

    def delete_all(self):
        insurances = self.query(GlobalInsurance).order_by(GlobalInsurance.id)
        for row in insurances:
            self.delete(row)
        self.commit()

    def add_random(self, insurer_controller):
        for i in range(1, 30):
            self.add(self.__generate_random(insurer_controller))
        self.commit()

    def max_id(self):
        insurances = self.query(GlobalInsurance).order_by(GlobalInsurance.id)
        return max(i.id for i in insurances)

    def __generate_random(self, insurer_controller):
        return GlobalInsurance(id=self.max_id() + 1,
                               insurer_id=int(random.uniform(1, 1 + max(i.id for i in insurer_controller.get_all()))),
                               expiration_date=generate_random_date(datetime.date.fromisoformat("2021-01-01"),
                                                                    datetime.date.fromisoformat("2023-12-12")))

    def add_insurance(self, insurance_id, insurer_id, expiration_date: datetime.date):
        self.add(GlobalInsurance(id=insurance_id,
                                 insurer_id=insurer_id,
                                 expiration_date=expiration_date))
        self.commit()

    def delete_insurance(self, insurance_id):
        insurance = self.query(GlobalInsurance).filter(GlobalInsurance.id == insurance_id)
        insurance.delete()
        self.commit()

# #init insurances after init insurers
# if __name__ == '__main__':
#     testInstance = InsuranceGlobalTest()
#     testInstance.getInsuranceGlobals()
#     testInstance.add_insurance(1, 1, datetime.date(2031, 1, 21))
#     testInstance.getInsuranceGlobals()
#     testInstance.delete_insurance(11)
#     testInstance.getInsuranceGlobals()
