from ui.delete_position import Ui_Dialog


class DelPositionDialog(Ui_Dialog):
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
        name = self.position_edit.text()
        try:
            self.__positions_controller.delete_position(name)
        except:
            self.__positions_controller.session.rollback()





