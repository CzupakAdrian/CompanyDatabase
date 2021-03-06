from sqlalchemy.engine import create_engine
from database_objects.Objects import Worker

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'albert_rio'  # enter your username
PASSWORD = 'albert'  # enter your password
HOST = 'localhost'  # enter the oracle db host url
PORT = 1521  # enter the oracle port number
SERVICE = 'ORCLCDB.localdomain'  # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD + '@' + HOST + ':' + str(
    PORT) + '/?service_name=' + SERVICE

engine = create_engine(ENGINE_PATH_WIN_AUTH, max_identifier_length=128)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
workers = session.query(Worker).all()
for worker in workers:
    print(worker.name)