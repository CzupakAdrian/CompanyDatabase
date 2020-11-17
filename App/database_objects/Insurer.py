from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Insurer(Base):
    __tablename__ = 'insurers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
