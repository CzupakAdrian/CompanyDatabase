from ui.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

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
        self.show_positions_btn.clicked.connect(self.__show_positions_btn_clicked)
        self.add_position_btn.clicked.connect(self.__add_position_btn_clicked)
        self.delete_position_btn.clicked.connect(self.__delete_position_btn_clicked)
        self.clear_btn.clicked.connect(self.__clear_btn_clicked)

    def __show_all_workers_btn_clicked(self):
        pass

    def __show_local_workers_btn_clicked(self):
        pass

    def __show_worker_btn_clicked(self):
        pass

    def __add_worker_btn_clicked(self):
        pass

    def __delete_worker_btn_clicked(self):
        pass

    def __show_all_preferences_btn_clicked(self):
        pass

    def __show_local_preferences_btn_clicked(self):
        pass

    def __show_worker_preference_btn_clicked(self):
        pass

    def __delete_preference_btn_clicked(self):
        pass

    def __add_preference_btn_clicked(self):
        pass

    def __show_insurances_btn_clicked(self):
        pass

    def __delete_insurance_btn_clicked(self):
        pass

    def __add_insurance_btn_clicked(self):
        pass

    def __show_positions_btn_clicked(self):
        pass

    def __add_position_btn_clicked(self):
        pass

    def __delete_position_btn_clicked(self):
        pass

    def __clear_btn_clicked(self):
        pass


