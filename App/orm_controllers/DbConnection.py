from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnectionAlbertRio:
    def __init__(self):
        self.DIALECT = 'oracle'
        self.SQL_DRIVER = 'cx_oracle'
        self.USERNAME = 'albert_rio'  # enter your username
        self.PASSWORD = 'albert'  # enter your password
        self.HOST = 'localhost'  # enter the oracle db host url
        self.PORT = 1521  # enter the oracle port number
        self.SERVICE = 'ORCLCDB.localdomain'  # enter the oracle db service name
        self.ENGINE_PATH_WIN_AUTH =\
            self.DIALECT + '+' + self.SQL_DRIVER + '://' +\
            self.USERNAME + ':' + self.PASSWORD + '@' + self.HOST + ':' +\
            str(self.PORT) + '/?service_name=' + self.SERVICE

        self.engine = create_engine(self.ENGINE_PATH_WIN_AUTH, max_identifier_length=128)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.session.bind


class DbConnectionAdrianTokyo:
    def __init__(self):
        self.DIALECT = 'oracle'
        self.SQL_DRIVER = 'cx_oracle'
        self.USERNAME = 'Master'  # enter your username
        self.PASSWORD = 'Master'  # enter your password
        self.HOST = 'localhost'  # enter the oracle db host url
        self.PORT = 1521  # enter the oracle port number
        self.SERVICE = 'ORCLCDB.localdomain'  # enter the oracle db service name
        self.ENGINE_PATH_WIN_AUTH =\
            self.DIALECT + '+' + self.SQL_DRIVER + '://' +\
            self.USERNAME + ':' + self.PASSWORD + '@' + self.HOST + ':' +\
            str(self.PORT) + '/?service_name=' + self.SERVICE

        self.engine = create_engine(self.ENGINE_PATH_WIN_AUTH, max_identifier_length=128)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.session.bind


class DbConnectionAdrianSarajevo:
    def __init__(self):
        self.DIALECT = 'oracle'
        self.SQL_DRIVER = 'cx_oracle'
        self.USERNAME = 'Master'  # enter your username
        self.PASSWORD = 'Master'  # enter your password
        self.HOST = 'localhost'  # enter the oracle db host url
        self.PORT = 1522  # enter the oracle port number
        self.SERVICE = 'ORCLCDB.localdomain'  # enter the oracle db service name
        self.ENGINE_PATH_WIN_AUTH =\
            self.DIALECT + '+' + self.SQL_DRIVER + '://' +\
            self.USERNAME + ':' + self.PASSWORD + '@' + self.HOST + ':' +\
            str(self.PORT) + '/?service_name=' + self.SERVICE

        self.engine = create_engine(self.ENGINE_PATH_WIN_AUTH, max_identifier_length=128)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.session.bind
