from PyQt5 import QtWidgets

from ui.main_window import Ui_MainWindow
from Test.TablesController import TablesController

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

    def __show_worker_btn_clicked(self):
        self.textEdit.clear()
        from ui.sh_worker import ShowWorkerDialog
        id = self.run_dialog_id(ShowWorkerDialog())
        if id > 0:
            try:
                worker = self.__tc.workers.get_worker(id)
                self.textEdit.append(f'Name: {worker.name}, Surname:{worker.surname}, Location: {worker.location.name}, '
                                     f'Position: {worker.position.position}, Insurance id: {worker.insurance_id}, '
                                     f'Birth_date: {worker.birth_date}')
            except:
                self.textEdit.append('Wrong id')

    def __delete_worker_btn_clicked(self):
        from ui.del_worker import DelWorkerDialog
        id = self.run_dialog_id(DelWorkerDialog())
        if id > 0:
            try:
                self.__tc.workers.delete_worker(id)
            except:
                self.textEdit.append('Wrong id')

    def __show_worker_preference_btn_clicked(self):
        self.textEdit.clear()
        from ui.sh_worker import ShowWorkerDialog
        id = self.run_dialog_id(ShowWorkerDialog())
        if id > 0:
            try:
                preference = self.__tc.preferences.get_preference(id)
                # self.textEdit.append(
                #     f'Name: {preference.worker.name}, Surname:{preference.worker.surname}, Current location: '
                #     f'{preference.worker.location.name}, '
                #     f'Position: {preference.worker.position.position}, Desired location: {preference.location.name}')

                from Test.GlobalWorkerPreferenceController import convert_to_pd_dataframe
                self.textEdit.setText(convert_to_pd_dataframe(preference).to_string())
            except:
                self.textEdit.append('Wrong id')

    def __show_insurances_btn_clicked(self):
        self.textEdit.clear()
        insurances = self.__tc.insurances.get_all()
        from Test.InsuranceController import convert_insurances_to_pd_dataframe
        insurances = convert_insurances_to_pd_dataframe(insurances).to_string()
        self.textEdit.append(insurances)

    def __delete_insurance_btn_clicked(self):
        from ui.del_insurance import DelInsuranceDialog
        id = self.run_dialog_id(DelInsuranceDialog())
        if id > 0:
            try:
                self.__tc.insurances.delete_insurance(id)
            except:
                self.__tc.connection.session.rollback()
                self.textEdit.setText('Wrong id')

    def __show_insurers_btn_clicked(self):
        self.textEdit.clear()
        insurers = self.__tc.insurers.get_all()
        from Test.InsurerController import convert_insurers_to_pd_dataframe
        insurers = convert_insurers_to_pd_dataframe(insurers).to_string()
        self.textEdit.append(insurers)

    def __add_insurer_btn_clicked(self):
        from ui.add_insurerr import AddInsurerDialog
        ui = AddInsurerDialog(self.__tc.insurers)
        self.run_dialog(ui)

    def __delete_insurer_btn_clicked(self):
        from ui.del_insurer import DelInsurerDialog
        id = self.run_dialog_id(DelInsurerDialog())
        if id > 0:
            try:
                self.__tc.insurers.delete_insurer(id)
            except:
                self.__tc.connection.session.rollback()
                self.textEdit.append('Wrong id')

    def __show_positions_btn_clicked(self):
        self.textEdit.clear()
        positions = self.__tc.positions.get_all()
        from Test.GlobalPositionController import convert_positions_to_pd_dataframe
        positions = convert_positions_to_pd_dataframe(positions).to_string()
        self.textEdit.append(positions)

    def __add_position_btn_clicked(self):
        from ui.add_pos import AddPositionDialog
        ui = AddPositionDialog(self.__tc.positions)
        self.run_dialog(ui)

    def __delete_position_btn_clicked(self):
        from ui.del_position import DelPositionDialog
        ui = DelPositionDialog(self.__tc.positions)
        self.run_dialog(ui)

    def __delete_preference_btn_clicked(self):
        from ui.del_preference import DelPreferenceDialog
        id = self.run_dialog_id(DelPreferenceDialog())
        if id > 0:
            try:
                self.__tc.preferences.delete_preference(id)
            except:
                self.__tc.connection.session.rollback()
                self.textEdit.append('Wrong id')

    def __add_preference_btn_clicked(self):
        from ui.add_pref import AddPreferenceDialog
        ui = AddPreferenceDialog(self.__tc.preferences)
        self.run_dialog(ui)

    def __show_all_preferences_btn_clicked(self):
        self.textEdit.clear()
        preferences = self.__tc.preferences.get_all()
        from Test.GlobalWorkerPreferenceController import convert_to_pd_dataframe
        preferences = convert_to_pd_dataframe(preferences)
        self.textEdit.append(preferences.to_string())

    def __show_local_preferences_btn_clicked(self):
        from Test.WorkerPreferenceController import convert_to_pd_dataframe
        self.textEdit.setText(convert_to_pd_dataframe(self.__tc.local_preferences.get_preferences()).to_string())

    def __add_worker_btn_clicked(self):
        from ui.add_work import AddWorkerDialog
        ui = AddWorkerDialog(self.__tc.workers)
        self.run_dialog(ui)

    def __show_local_workers_btn_clicked(self):
        self.textEdit.clear()
        workers = self.__tc.local_workers.get_all()
        from Test.WorkerController import convert_workers_to_pd_dataframe
        workers = convert_workers_to_pd_dataframe(workers)
        self.textEdit.append(workers.to_string())

    def __add_insurance_btn_clicked(self):
        from ui.add_ins import AddInsuranceDialog
        ui = AddInsuranceDialog(self.__tc.insurances)
        self.run_dialog(ui)

    def __clear_btn_clicked(self):
        self.textEdit.clear()

    def run_dialog_id(self, ui):
        dialog = QtWidgets.QDialog()
        ui.setupUi(dialog)
        dialog.show()
        id = dialog.exec_()
        return id

    def run_dialog(self, ui):
        dialog = QtWidgets.QDialog()
        ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()


