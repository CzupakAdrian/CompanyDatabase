from ui.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        self.__connectSlots()

    def __connectSlots(self):
        self.show_all_workers_btn.clicked.connect(self.__show_all_workers_btn_clicked)

    def __show_all_workers_btn_clicked(self):
        pass



