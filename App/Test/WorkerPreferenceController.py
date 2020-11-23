from orm_controllers.DbConnection import DbConnectionAlbertSarajevo, DbConnectionAdrianSarajevo
from database_objects.Objects import WorkerPreference
from orm_controllers.BaseController import BaseController
import pandas as pd


def convert_to_pd_dataframe(prefs):
    workers_preferences_list = [(preference.worker_id, preference.worker.name, preference.worker.surname,
                                 preference.worker.position.position, preference.worker.location.name,
                                 preference.location.name) for preference in prefs]
    return pd.DataFrame(workers_preferences_list, columns=['worker id', 'worker name', 'worker surname',
                                                           'current position', 'current localization',
                                                           'desired localization'])


# Read only class
class WorkerPreferenceController(BaseController):
    def __init__(self, db_connection):
        super().__init__(db_connection)

    def get_preferences(self):
        prefs = self.query(WorkerPreference).order_by(WorkerPreference.worker_id)
        return prefs

    def get_preference(self, worker_id):
        return self.query(WorkerPreference).get(worker_id)


if __name__ == '__main__':
    testInstance = WorkerPreferenceController(DbConnectionAdrianSarajevo())
    preferences = testInstance.get_preferences()
    print(convert_to_pd_dataframe(preferences))
