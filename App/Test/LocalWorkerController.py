from datetime import date

from orm_controllers.DbConnection import DbConnectionAdrianSarajevo
from database_objects.Objects import Worker, Position, Location, GlobalInsurance
from orm_controllers.BaseController import BaseController
from Test.GlobalPositionController import convert_positions_to_pd_dataframe
from Test.LocationController import convert_locations_to_pd_dataframe
from Test.InsuranceController import convert_insurances_to_pd_dataframe
import names
from Test.InsuranceController import generate_random_date
import datetime
import random
from Test.WorkerController import convert_workers_to_pd_dataframe


# Read only class
class LocalWorkerController(BaseController):
    def __init__(self, connection):
        super().__init__(connection)

    def get_all(self):
        return self.query(Worker).order_by(Worker.id)

    def get_worker(self, worker_id):
        return self.query(Worker).get(worker_id)


if __name__ == '__main__':
    testInstance = LocalWorkerController(DbConnectionAdrianSarajevo())
    workers = testInstance.get_all()
    print(convert_workers_to_pd_dataframe(workers))
    worker = testInstance.get_worker(2)
    print(worker.name)
