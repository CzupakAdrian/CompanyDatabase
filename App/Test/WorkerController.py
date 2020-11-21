from datetime import date

from orm_controllers.DbConnection import DbConnectionAlbertSarajevo
from database_objects.Objects import GlobalWorker
from database_objects.Objects import Position
from orm_controllers.BaseController import BaseController
import pandas as pd
import names
from Test.InsuranceController import generate_random_date
import datetime
import random


def convert_to_pd_dataframe(workers):
    workers_list = [(worker.id, worker.name, worker.surname, worker.birth_date, worker.position.position,
                     worker.location.name, worker.insurance_id) for worker in workers]
    return pd.DataFrame(workers_list, columns=['id', 'name', 'surname', 'birth date', 'position', 'localization',
                                               'insurance id'])


# Read only class
class WorkerController(BaseController):
    def __init__(self, connection):
        super().__init__(connection)

    def get_all(self):
        return self.query(GlobalWorker).order_by(GlobalWorker.id)
        #return pd.read_sql_query(workers.statement, con=self.conn, index_col='id')

    def delete_worker(self, worker_id):
        insurer = self.query(GlobalWorker).get(worker_id)
        self.delete(insurer)
        self.commit()

    def __generate_random(self, location_controller, insurance_controller):
        return GlobalWorker(id=2,
                            name=names.get_first_name(),
                            surname=names.get_last_name(),
                            birth_date=generate_random_date(datetime.date.fromisoformat("1955-01-01"),
                                                            datetime.date.fromisoformat("2000-12-12")),
                            position_id=int(random.uniform(1, max(i.id for i in self.query(Position)))),
                            location_id=int(random.uniform(1, max(i.id for i in location_controller.get_all()))),
                            insurance_id=int(random.uniform(1, max(i.id for i in insurance_controller.get_all()))))

    def add_random(self, location_controller, insurance_controller):
        for i in range(1, 40):
            self.add(self.__generate_random(location_controller, insurance_controller))
        self.commit()

    def get_worker(self, worker_id):
        return self.query(GlobalWorker).get(worker_id)


if __name__ == '__main__':
    testInstance = WorkerController(DbConnectionAlbertSarajevo())
    workers = testInstance.get_all()
    print(convert_to_pd_dataframe(workers))
    worker = testInstance.get_worker(1)
    print(worker.name)