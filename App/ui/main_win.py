from PyQt5 import QtWidgets

from Test.TablesController import TablesController
from ui.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self, db_connection):
        super(MainWindow, self).__init__()
        self.__tc = TablesController(db_connection)

    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        self.__connectSlots()

    def __connectSlots(self):
        self.show_all_workers_btn.clicked.connect(self.__show_all_workers_btn_clicked)
        self.show_local_workers_btn.clicked.connect(self.__show_local_workers_btn_clicked)
        self.show_worker_btn.clicked.connect(self.__show_worker_btn_clicked)
        self.add_worker_btn.clicked.connect(self.__add_worker_btn_clicked)
        self.delete_worker_btn.clicked.connect(self.__delete_worker_btn_clicked)
        self.show_all_preferences_btn.clicked.connect(self.__show_all_preferences_btn_clicked)
        self.show_local_preferences_btn.clicked.connect(self.__show_local_preferences_btn_clicked)
        self.show_worker_preference_btn.clicked.connect(self.__show_worker_preference_btn_clicked)
        self.delete_preference_btn.clicked.connect(self.__delete_preference_btn_clicked)
        self.add_preference_btn.clicked.connect(self.__add_preference_btn_clicked)
        self.show_insurances_btn.clicked.connect(self.__show_insurances_btn_clicked)
        self.delete_insurance_btn.clicked.connect(self.__delete_insurance_btn_clicked)
        self.add_insurance_btn.clicked.connect(self.__add_insurance_btn_clicked)
        self.show_insurers_btn.clicked.connect(self.__show_insurers_btn_clicked)
        self.add_insurer_btn.clicked.connect(self.__add_insurer_btn_clicked)
        self.delete_insurer_btn.clicked.connect(self.__delete_insurer_btn_clicked)
        self.show_positions_btn.clicked.connect(self.__show_positions_btn_clicked)
        self.add_position_btn.clicked.connect(self.__add_position_btn_clicked)
        self.delete_position_btn.clicked.connect(self.__delete_position_btn_clicked)
        self.clear_btn.clicked.connect(self.__clear_btn_clicked)

    def __show_all_workers_btn_clicked(self):
        self.textEdit.clear()
        workers = self.__tc.workers.get_all()
        from Test.WorkerController import convert_workers_to_pd_dataframe
        workers = convert_workers_to_pd_dataframe(workers)
        self.textEdit.append(workers.to_string())

    def __show_local_workers_btn_clicked(self):
        pass

    def __show_worker_btn_clicked(self):
        self.textEdit.clear()
        dialog = QtWidgets.QDialog()
        from ui.sh_worker import ShowWorkerDialog
        ui = ShowWorkerDialog()
        ui.setupUi(dialog)
        dialog.show()
        id = dialog.exec_()
        if id > 0:
            try:
                worker = self.__tc.workers.get_worker(id)
                self.textEdit.append(f'Name: {worker.name}, Surname:{worker.surname}, Location: {worker.location.name}, '
                                     f'Position: {worker.position.position}, Insurance id: {worker.insurance_id}, '
                                     f'Birth_date: {worker.birth_date}')
            except:
                self.textEdit.append('Wrong id')

    def __add_worker_btn_clicked(self):
        pass

    def __delete_worker_btn_clicked(self):
        dialog = QtWidgets.QDialog()
        from ui.del_worker import DelWorkerDialog
        ui = DelWorkerDialog()
        ui.setupUi(dialog)
        dialog.show()
        id = dialog.exec_()
        if id > 0:
            try:
                self.__tc.workers.delete_worker(id)
            except:
                self.textEdit.append('Wrong id')

    def __show_all_preferences_btn_clicked(self):
        pass

    def __show_local_preferences_btn_clicked(self):
        pass

    def __show_worker_preference_btn_clicked(self):
        self.textEdit.clear()
        dialog = QtWidgets.QDialog()
        from ui.sh_worker import ShowWorkerDialog
        ui = ShowWorkerDialog()
        ui.setupUi(dialog)
        dialog.show()
        id = dialog.exec_()
        if id > 0:
            try:
                preference = self.__tc.preferences.get_preference(id)
                self.textEdit.append(
                    f'Name: {preference.worker.name}, Surname:{preference.worker.surname}, Current location: '
                    f'{preference.worker.location.name}, '
                    f'Position: {preference.worker.position.position}, Desired location: {preference.location.name}')
            except:
                self.textEdit.append('Wrong id')

    def __delete_preference_btn_clicked(self):
        pass

    def __add_preference_btn_clicked(self):
        pass

    def __show_insurances_btn_clicked(self):
        self.textEdit.clear()
        insurances = self.__tc.insurances.get_all()
        from Test.InsuranceController import convert_insurances_to_pd_dataframe
        insurances = convert_insurances_to_pd_dataframe(insurances).to_string()
        self.textEdit.append(insurances)

    def __delete_insurance_btn_clicked(self):
        pass

    def __add_insurance_btn_clicked(self):
        pass

    def __show_insurers_btn_clicked(self):
        self.textEdit.clear()
        insurers = self.__tc.insurers.get_all()
        from Test.InsurerController import convert_insurers_to_pd_dataframe
        insurers = convert_insurers_to_pd_dataframe(insurers).to_string()
        self.textEdit.append(insurers)

    def __add_insurer_btn_clicked(self):
        pass

    def __delete_insurer_btn_clicked(self):
        pass

    def __show_positions_btn_clicked(self):
        self.textEdit.clear()
        positions = self.__tc.positions.get_all()
        from Test.GlobalPositionController import convert_positions_to_pd_dataframe
        positions = convert_positions_to_pd_dataframe(positions).to_string()
        self.textEdit.append(positions)

    def __add_position_btn_clicked(self):
        pass

    def __delete_position_btn_clicked(self):
        pass

    def __clear_btn_clicked(self):
        self.textEdit.clear()


