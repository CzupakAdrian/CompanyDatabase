from datetime import date

from orm_controllers.DbConnection import DbConnectionAlbertSarajevo
from database_objects.Objects import WorkerPreference
import pandas as pd


def convert_to_pd_dataframe(prefs):
    workers_preferences_list = [(preference.worker_id, preference.worker.name, preference.worker.surname,
                                 preference.worker.position.position, preference.worker.location.name,
                                 preference.location.name) for preference in prefs]
    return pd.DataFrame(workers_preferences_list, columns=['worker id', 'worker name', 'worker surname',
                                                           'current position', 'current localization',
                                                           'desired localization'])


# Read only class
class WorkerPreferenceTest:
    def __init__(self, db_connection):
        self.session = db_connection.get_session()

    def get_preferences(self):
        prefs = self.session.query(WorkerPreference).order_by(WorkerPreference.worker_id)
        return prefs

    def get_preference(self, worker_id):
        return self.session.query(WorkerPreference).get(worker_id)


if __name__ == '__main__':
    testInstance = WorkerPreferenceTest(DbConnectionAlbertSarajevo())
    preferences = testInstance.get_preferences()
    print(convert_to_pd_dataframe(preferences))
