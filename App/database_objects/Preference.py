from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Preference(Base):
    __tablename__ = 'preferences'
    current_location_id = Column(Integer)
    worker_id = Column(Integer)
    prefered_location_id = Column(Integer)
