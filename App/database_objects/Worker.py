from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    position_id = Column(Integer, nullable=False)
    location_id = Column(Integer)
    insurance_id = Column(Integer)
