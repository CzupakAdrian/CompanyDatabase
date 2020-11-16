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
        from sqlalchemy.engine import create_engine

        DIALECT = 'oracle'
        SQL_DRIVER = 'cx_oracle'
        USERNAME = 'albert_rio'  # enter your username
        PASSWORD = 'albert'  # enter your password
        HOST = 'localhost'  # enter the oracle db host url
        PORT = 1521  # enter the oracle port number
        SERVICE = 'ORCLCDB.localdomain'  # enter the oracle db service name
        ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(
            PORT) + '/?service_name=' + SERVICE

        engine = create_engine(ENGINE_PATH_WIN_AUTH)

        # import pandas as pd
        # test_df = pd.read_sql_query('SELECT * FROM global_name', engine)
        # print(test_df)



