from ui.add_worker import Ui_Dialog


class AddWorkerDialog(Ui_Dialog):
    def __init__(self, workers_controller):
        super(Ui_Dialog, self).__init__()
        self.__workers_controller = workers_controller

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.dial = Dialog
        self.__connect_slots()

    def __connect_slots(self):
        self.buttonBox.accepted.connect(self.__accept_btn_clicked)

    def __accept_btn_clicked(self):
        name = self.edit_name.text()
        surname = self.edit_surname.text()
        date_ = self.edit_date.date().toPyDate()
        insurance_id = int(self.edit_insurance.text())
        location_id = int(self.edit_location.text())
        position_id = int(self.edit_position.text())
        self.__workers_controller.add_worker(name, surname, date_,
                                             position_id, location_id,
                                             insurance_id)





