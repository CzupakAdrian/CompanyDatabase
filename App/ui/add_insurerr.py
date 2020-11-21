from ui.add_insurer import Ui_Dialog


class AddInsurerDialog(Ui_Dialog):
    def __init__(self, insurers_controller):
        super(Ui_Dialog, self).__init__()
        self.__insurers_controller = insurers_controller

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.dial = Dialog
        self.__connect_slots()

    def __connect_slots(self):
        self.buttonBox.accepted.connect(self.__accept_btn_clicked)

    def __accept_btn_clicked(self):
        name = self.name_edit.text()
        self.__insurers_controller.add_insurer(name)





