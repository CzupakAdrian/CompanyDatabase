from ui.delete_insurer import Ui_Dialog


class DelInsurerDialog(Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.dial = Dialog
        self.__connect_slots()

    def __connect_slots(self):
        self.buttonBox.accepted.connect(self.__accept_btn_clicked)

    def __accept_btn_clicked(self):
        self.dial.done(self.id_box.value())





