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

engine = create_engine(ENGINE_PATH_WIN_AUTH, max_identifier_length=128)

from database_objects.Location import Location
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
locations = session.query(Location).order_by(Location.id)
# for location in locations:
#     print(location.id, location.name)
# to pandas dataframe
import pandas as pd
conn = session.bind
df = pd.read_sql_query(locations.statement, con=conn, index_col='id')
print(df)
