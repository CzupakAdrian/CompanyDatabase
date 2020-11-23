from ui.add_preference import Ui_Dialog


class AddPreferenceDialog(Ui_Dialog):
    def __init__(self, preferences_controller):
        super(Ui_Dialog, self).__init__()
        self.__preferences_controller = preferences_controller

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.dial = Dialog
        self.__connect_slots()

    def __connect_slots(self):
        self.buttonBox.accepted.connect(self.__accept_btn_clicked)

    def __accept_btn_clicked(self):
        worker_id = int(self.edit_worker.text())
        location_id = int(self.edit_location.text())
        self.__preferences_controller.add_preference(worker_id, location_id)





