from ui.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        self.__connectSlots()

    def __connectSlots(self):
        self.connect_btn.clicked.connect(self.__connect_btn_clicked)

    def __connect_btn_clicked(self):
        pass



