from orm_controllers.DbConnection import DbConnectionAlbertSarajevo
from database_objects.Objects import GlobalWorkerPreference
import pandas as pd


def convert_to_pd_dataframe(prefs):
    workers_preferences_list = [(preference.worker_id, preference.worker.name, preference.worker.surname,
                                 preference.worker.position.position, preference.worker.location.name,
                                 preference.location.name) for preference in prefs]
    return pd.DataFrame(workers_preferences_list, columns=['worker id', 'worker name', 'worker surname',
                                                           'current position', 'current localization',
                                                           'desired localization'])


class GlobalWorkerPreferenceTest:
    def __init__(self, db_connection):
        self.session = db_connection.get_session()

    def get_preferences(self):
        prefs = self.session.query(GlobalWorkerPreference)#.order_by(GlobalWorkerPreference.worker_id)
        return prefs

    def get_preference(self, worker_id):
        return self.session.query(GlobalWorkerPreference).get(worker_id)

    def add_preference(self, worker_id, location_id):
        self.session.add(GlobalWorkerPreference(worker_id=worker_id, location_id=location_id))
        self.session.commit()

    # def delete_preference(self, worker_id, location_id):
    #     position = self.session.query(GlobalPosition).get(name)
    #     self.session.delete(position)
    #     self.session.commit()


if __name__ == '__main__':
    testInstance = GlobalWorkerPreferenceTest(DbConnectionAlbertSarajevo())
    # prefs = testInstance.get_preferences()
    # print(convert_to_pd_dataframe(prefs))
    # pref = testInstance.get_preference(1)
    # print(pref.worker.name)
    # testInstance.add_preference(2, 2)

    # Cuts all duplicates
    prefs = testInstance.get_preferences()
    print(convert_to_pd_dataframe(prefs))
