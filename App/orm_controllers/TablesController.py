from orm_controllers.DbConnection import DbConnection
from database_objects.Objects import Insurer, GlobalInsurance, Worker, Location, GlobalPosition, GlobalWorkerPreference

class TablesController(DbConnection):
    def __init__(self):
        super().__init__()

    def getAllGlobalInsurances(self):
        print(self.session.query(GlobalInsurance.id, GlobalInsurance.expiration_date, Insurer.name).
              filter(GlobalInsurance.insurer_id == Insurer.id).all())

    def getAllWorkers(self):
        print(self.session.query(Worker.name, Worker.surname, Worker.birth_date, Location.name,
                                 GlobalPosition.position, GlobalInsurance.expiration_date, Insurer.name)
              .filter(Worker.location_id == Location.id)
              .filter(Worker.position_id == GlobalPosition.id)
              .filter(Worker.insurance_id == GlobalInsurance.id)
              .filter(GlobalInsurance.insurer_id == Insurer.id)
              .all())

    def getAllPrefs(self):
        print(self.session.query(GlobalWorkerPreference.worker.name,
                                 GlobalWorkerPreference.worker.surname,
                                 GlobalWorkerPreference.location.name))

    def getPropsFor(self, worker):
        print(self.session.query(GlobalWorkerPreference.worker.name,
                                 GlobalWorkerPreference.worker.surname,
                                 GlobalWorkerPreference.location.name).
              filter(GlobalWorkerPreference.worker.position_id == worker.position_id).
              filter(GlobalWorkerPreference.location_id == worker.location_id))


if __name__ == '__main__':
    testInstance = TablesController()
    testInstance.getAllWorkers()
