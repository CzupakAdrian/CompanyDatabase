from Test.InsurerController import InsurerController
from Test.InsuranceController import InsuranceController
from Test.LocationController import LocationController
from Test.GlobalPositionController import GlobalPositionController
from Test.WorkerController import WorkerController
from Test.GlobalWorkerPreferenceController import GlobalWorkerPreferenceController

class TablesController():
    def __init__(self, connection):
        self.connection = connection
        self.insurers = InsurerController(connection)
        self.locations = LocationController(connection)
        self.insurances = InsuranceController(connection)
        self.positions = GlobalPositionController(connection)
        self.workers = WorkerController(connection)
        self.preferences = GlobalWorkerPreferenceController(connection)

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
    # def getPropsFor(self, worker):
    #     print(self.session.query(GlobalWorkerPreference.worker.name,
    #                              GlobalWorkerPreference.worker.surname,
    #                              GlobalWorkerPreference.location.name).
    #           filter(GlobalWorkerPreference.worker.position_id == worker.position_id).
    #           filter(GlobalWorkerPreference.location_id == worker.location_id))


# if __name__ == '__main__':
#     testInstance = TablesController()
#     testInstance.getAllWorkers()
