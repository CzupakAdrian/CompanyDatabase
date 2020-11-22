from ui.add_position import Ui_Dialog


class AddPositionDialog(Ui_Dialog):
    def __init__(self, positions_controller):
        super(Ui_Dialog, self).__init__()
        self.__positions_controller = positions_controller

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.dial = Dialog
        self.__connect_slots()

    def __connect_slots(self):
        self.buttonBox.accepted.connect(self.__accept_btn_clicked)

    def __accept_btn_clicked(self):
        name = self.name_edit.text()
        self.__positions_controller.add_position(name)





