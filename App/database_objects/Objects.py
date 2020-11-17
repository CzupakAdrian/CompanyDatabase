from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)
    position_id = Column(Integer)
    location_id = Column(Integer, ForeignKey('locations.id'))
    insurance_id = Column(Integer)

    location = relationship('Location')


class Insurer(Base):
    __tablename__ = 'insurers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Modify to vertical fragmentation
class Insurance(Base):
    __tablename__ = 'insurances'
    id = Column(Integer, primary_key=True)
    insurer_id = Column(Integer, ForeignKey('insurers.id'))
    expiration_date = Column(Date)


class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    position = Column(String)


class WorkerPreference(Base):
    __tablename__ = 'workers_preferences'
    worker_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))

    worker = relationship('Worker')
    location = relationship('Location')


class GlobalWorker(Base):
    __tablename__ = 'all_workers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)
    position_id = Column(Integer)
    location_id = Column(Integer, ForeignKey('locations.id'))
    insurance_id = Column(Integer)

    location = relationship('Location')


class GlobalWorkerPreference(Base):
    __tablename__ = 'all_preferences'
    worker_id = Column(Integer, ForeignKey('all_workers.id'), primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))

    worker = relationship('GlobalWorker')
    location = relationship('Location')
