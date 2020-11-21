from Test.InsurerController import InsurerController
from Test.InsuranceController import InsuranceController
from Test.LocationController import LocationController
from Test.GlobalPositionController import GlobalPositionController
from Test.WorkerController import WorkerController, convert_workers_to_pd_dataframe
from Test.GlobalWorkerPreferenceController import GlobalWorkerPreferenceController
from database_objects.Objects import GlobalWorkerPreference, GlobalWorker, Location
from orm_controllers.DbConnection import DbConnectionAdrianSarajevo
import pandas as pd
import datetime


class TablesController():
    def __init__(self, connection):
        self.connection = connection
        self.query = connection.session.query
        self.insurers = InsurerController(connection)
        self.locations = LocationController(connection)
        self.insurances = InsuranceController(connection)
        self.positions = GlobalPositionController(connection)
        self.workers = WorkerController(connection)
        self.preferences = GlobalWorkerPreferenceController(connection)
    # DO OGARNIĘCIA JESZCZE
    # def get_possible_exchanges(self):
    #     exchange_possibilities = list()
    #     workers = self.query(GlobalWorker).filter(
    #         GlobalWorker.id == GlobalWorkerPreference.worker_id)
    #     for wor in workers:
    #         exchange_possibilities.append(self.getPropsFor(wor))
    #     return exchange_possibilities
    #
    #
    # def getPropsFor(self, worker):
    #     workers = self.query(GlobalWorker.name,
    #                          GlobalWorker.surname,
    #                          Location.name).\
    #         filter(GlobalWorker.position_id == worker.position_id).\
    #         filter(GlobalWorker.id == GlobalWorkerPreference.worker_id).\
    #         filter(GlobalWorkerPreference.location_id == worker.location_id).\
    #         filter(Location.id == GlobalWorker.location_id)
    #     workers_list = [(worker.name,
    #                      worker.surname,
    #                      worker.location.name,
    #                      new_worker.worker.name,
    #                      new_worker.worker.surname,
    #                      new_worker.worker.location.name)
    #                     for new_worker in workers]
    #     return pd.DataFrame(workers_list, columns=['name1', 'surname1', 'location1',
    #                                                'name2', 'surname2', 'location2'])

    # def getAllGlobalInsurances(self):
    #     print(self.session.query(GlobalInsurance.id, GlobalInsurance.expiration_date, Insurer.name).
    #           filter(GlobalInsurance.insurer_id == Insurer.id).all())
    #
    # def getAllWorkers(self):
    #     print(self.session.query(Worker.name, Worker.surname, Worker.birth_date, Location.name,
    #                              GlobalPosition.position, GlobalInsurance.expiration_date, Insurer.name)
    #           .filter(Worker.location_id == Location.id)
    #           .filter(Worker.position_id == GlobalPosition.id)
    #           .filter(Worker.insurance_id == GlobalInsurance.id)
    #           .filter(GlobalInsurance.insurer_id == Insurer.id)
    #           .all())
    #
    # def getAllPrefs(self):
    #     print(self.session.query(GlobalWorkerPreference.worker.name,
    #                              GlobalWorkerPreference.worker.surname,
    #                              GlobalWorkerPreference.location.name))
    #


if __name__ == '__main__':
    testInstance = TablesController(DbConnectionAdrianSarajevo())
    # print(testInstance.getPropsFor(GlobalWorker(id=126,
    #                                             name='Cindy',
    #                                             surname='Bennet',
    #                                             position_id=4,
    #                                             location_id=2
    #                                             )))
    # print(testInstance.get_possible_exchanges())
