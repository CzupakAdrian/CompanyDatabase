from datetime import date

from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import GlobalWorker
import pandas as pd


def convert_to_pd_dataframe(workers):
    workers_list = [(worker.id, worker.name, worker.surname, worker.birth_date, worker.position.position,
                     worker.location.name, worker.insurance_id) for worker in workers]
    return pd.DataFrame(workers_list, columns=['id', 'name', 'surname', 'birth date', 'position', 'localization',
                                               'insurance id'])


class GlobalWorkerTest(DbConnection):
    def __init__(self):
        super().__init__()

    def get_workers(self):
        workers = self.session.query(GlobalWorker).order_by(GlobalWorker.id)
        return workers
        # print(pd.read_sql_query(prefs.statement, con=self.conn, index_col='id'))

    def delete_all_workers(self):
        workers = self.session.query(GlobalWorker).order_by(GlobalWorker.id)
        for row in workers:
            self.session.delete(row)
        self.session.commit()

    def get_worker(self, worker_id):
        return self.session.query(GlobalWorker).get(worker_id)

    def add_worker(self, name, surname, birth_date, position_id, location_id, insurance_id):
        AUTOGENERATE = 0
        self.session.add(GlobalWorker(id=AUTOGENERATE, name=name, surname=surname, birth_date=birth_date,
                                      position_id=position_id, location_id=location_id, insurance_id=insurance_id))
        self.session.commit()

    def delete_worker(self, worker_id):
        worker = self.session.query(GlobalWorker).get(worker_id)
        self.session.delete(worker)
        self.session.commit()


if __name__ == '__main__':
    testInstance = GlobalWorkerTest()
    workers = testInstance.get_workers()
    print(convert_to_pd_dataframe(workers))
    testInstance.add_worker('Brianek', 'Patusinski', date(2000, 1, 1), 1, 2, 1)
    workers = testInstance.get_workers()
    print(convert_to_pd_dataframe(workers))
    # testInstance.delete_worker(2)
    # print(convert_to_pd_dataframe(workers))


