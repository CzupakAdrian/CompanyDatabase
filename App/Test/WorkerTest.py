from datetime import date

from orm_controllers.DbConnection import DbConnectionAlbertSarajevo
from database_objects.Objects import GlobalWorker
import pandas as pd


def convert_to_pd_dataframe(workers):
    workers_list = [(worker.id, worker.name, worker.surname, worker.birth_date, worker.position.position,
                     worker.location.name, worker.insurance_id) for worker in workers]
    return pd.DataFrame(workers_list, columns=['id', 'name', 'surname', 'birth date', 'position', 'localization',
                                               'insurance id'])


# Read only class
class WorkerTest:
    def __init__(self, db_connection):
        self.session = db_connection.get_session()

    def get_workers(self):
        workers = self.session.query(GlobalWorker).order_by(GlobalWorker.id)
        return workers
        # print(pd.read_sql_query(prefs.statement, con=self.conn, index_col='id'))

    def get_worker(self, worker_id):
        return self.session.query(GlobalWorker).get(worker_id)


if __name__ == '__main__':
    testInstance = WorkerTest(DbConnectionAlbertSarajevo())
    workers = testInstance.get_workers()
    print(convert_to_pd_dataframe(workers))
    worker = testInstance.get_worker(1)
    print(worker.name)