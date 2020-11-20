from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnection:
    def __init__(self):
        self.DIALECT = 'oracle'
        self.SQL_DRIVER = 'cx_oracle'
        self.HOST = 'localhost'  # enter the oracle db host url
        self.SERVICE = 'ORCLCDB.localdomain'  # enter the oracle db service name
        self.USERNAME = ''  # enter your username
        self.PASSWORD = ''  # enter your password
        self.PORT = 1521  # enter the oracle port number

    def establish_connection(self):
        self.ENGINE_PATH_WIN_AUTH = self.DIALECT + '+' + self.SQL_DRIVER + '://' + self.USERNAME + ':' + self.PASSWORD \
                                    + '@' + self.HOST + ':' + str(self.PORT) + '/?service_name=' + self.SERVICE
        self.engine = create_engine(self.ENGINE_PATH_WIN_AUTH, max_identifier_length=128)
        self.session = sessionmaker(bind=self.engine)()
        self.conn = self.session.bind

    def get_session(self):
        return self.session

    def get_connection(self):
        return self.conn


class DbConnectionAlbertSarajevo(DbConnection):
    def __init__(self):
        super().__init__()
        self.USERNAME = 'albert_rio'  # old user from rio :)
        self.PASSWORD = 'albert'
        self.establish_connection()


class DbConnectionAlbertTokyo(DbConnection):
    def __init__(self):
        super().__init__()
        self.USERNAME = 'albert_tokyo'  # enter your username
        self.PASSWORD = 'albert'  # enter your password
        self.PORT = 1522  # enter the oracle port number
        self.establish_connection()


class DbConnectionAdrianTokyo(DbConnection):
    def __init__(self):
        super(DbConnectionAdrianTokyo, self).__init__()
        self.USERNAME = 'Master'  # enter your username
        self.PASSWORD = 'Master'  # enter your password
        self.establish_connection()


class DbConnectionAdrianSarajevo(DbConnection):
    def __init__(self):
        super().__init__()
        self.USERNAME = 'Master'  # enter your username
        self.PASSWORD = 'Master'  # enter your password
        self.PORT = 1522  # enter the oracle port number
        self.establish_connection()

