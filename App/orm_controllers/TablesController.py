from DbConnection import DbConnection
from Objects import Insurer, Insurance, Worker, Location, Position
import pandas as pd

class TablesController(DbConnection):
    def __init__(self):
        super().__init__()

    def getAllInsurances(self):
        print(self.session.query(Insurance.id, Insurance.expiration_date, Insurer.name).\
                filter(Insurance.insurer_id == Insurer.id).all())

    def getAllWorkers(self):
        print(self.session.query(Worker.name, Worker.surname, Worker.birth_date, Location.name,
                                 Position.position, Insurance.expiration_date, Insurer.name)
              .filter(Worker.location_id == Location.id)
              .filter(Worker.position_id == Position.id)
              .filter(Worker.insurance_id == Insurance.id)
              .filter(Insurance.insurer_id == Insurer.id)
              .all())


if __name__ == '__main__':
    testInstance = TablesController()
    testInstance.getAllWorkers()
