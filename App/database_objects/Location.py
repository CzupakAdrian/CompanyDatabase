from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Location(Base):
    __tablename__ = 'all_workers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
