from ui.add_insurance import Ui_Dialog


class AddInsuranceDialog(Ui_Dialog):
    def __init__(self, insurances_controller):
        super(Ui_Dialog, self).__init__()
        self.__insurances_controller = insurances_controller

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.dial = Dialog
        self.__connect_slots()

    def __connect_slots(self):
        self.buttonBox.accepted.connect(self.__accept_btn_clicked)

    def __accept_btn_clicked(self):
        date_ = self.date.date().toPyDate()
        insurer_id = int(self.insurer.text())
        insurance_id = int(self.id.text())
        self.__insurances_controller.add_insurance(insurance_id, insurer_id, date_)





