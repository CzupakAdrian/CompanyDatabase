from ui.main_window import Ui_MainWindow
from orm_controllers.DbConnection import DbConnectionAdrianSarajevo
from Test.TablesController import TablesController
from Test.WorkerController import convert_workers_to_pd_dataframe
from Test.GlobalWorkerPreferenceController import convert_preferences_to_pd_dataframe

class MainWindow(Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

    def setupUi(self, mainWindow):
        super().setupUi(mainWindow)
        self.controller = TablesController(DbConnectionAdrianSarajevo())
        self.__connectSlots()

    def __connectSlots(self):
        self.show_all_workers_btn.clicked.connect(self.__show_all_workers_btn_clicked)
        self.show_all_preferences_btn.clicked.connect(self.__show_all_preferences_btn_clicked)
        self.show_local_preferences_btn.clicked.connect(self.__sho_possible_exchange_btn_clicked) #change button name

    def __show_all_workers_btn_clicked(self):
        self.textEdit.setText(convert_workers_to_pd_dataframe(self.controller.workers.get_all()).to_string())

    def __show_all_preferences_btn_clicked(self):
        self.textEdit.setText(convert_preferences_to_pd_dataframe(self.controller.preferences.get_all()).to_string())

    def __sho_possible_exchange_btn_clicked(self):
        self.textEdit.setText(convert_preferences_to_pd_dataframe(self.controller.get_possible_exchanges()).to_string())



