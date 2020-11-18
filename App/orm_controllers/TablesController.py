from orm_controllers.DbConnection import DbConnection
<<<<<<< HEAD
from database_objects.Objects import Insurer, GlobalInsurance, Worker, Location, Position
=======
from database_objects.Objects import InsurerLocal, GlobalInsurance, Worker, Location, Position
>>>>>>> d99846acdc24a3cf0352ae571f75e96d27ef486f


class TablesController(DbConnection):
    def __init__(self):
        super().__init__()

    def getAllGlobalInsurances(self):
        print(self.session.query(GlobalInsurance.id, GlobalInsurance.expiration_date, Insurer.name). \
              filter(GlobalInsurance.insurer_id == Insurer.id).all())

    def getAllWorkers(self):
        print(self.session.query(Worker.name, Worker.surname, Worker.birth_date, Location.name,
                                 Position.position, GlobalInsurance.expiration_date, Insurer.name)
              .filter(Worker.location_id == Location.id)
              .filter(Worker.position_id == Position.id)
              .filter(Worker.insurance_id == GlobalInsurance.id)
              .filter(GlobalInsurance.insurer_id == Insurer.id)
              .all())


if __name__ == '__main__':
    testInstance = TablesController()
    testInstance.getAllWorkers()
