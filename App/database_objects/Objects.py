from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import PrimaryKeyConstraint

Base = declarative_base()


# Read only
class Location(Base):
    __tablename__ = 'locations'
    id = Column(Integer, primary_key=True)
    name = Column(String)


# Read only
class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)
    position_id = Column(Integer, ForeignKey('positions.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    insurance_id = Column(Integer, ForeignKey('insurances.id'))

    location = relationship('Location')
    position = relationship('Position')


# Read only
class WorkerPreference(Base):
    __tablename__ = 'workers_preferences'
    worker_id = Column(Integer, ForeignKey('workers.id'), primary_key=True)
    location_id = Column(Integer, ForeignKey('locations.id'))

    worker = relationship('Worker')
    location = relationship('Location')


# Read and write
class Insurer(Base):
    __tablename__ = 'insurers_local'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Position(Base):
    __tablename__ = 'positions'
    id = Column(Integer, primary_key=True)
    position = Column(String)

# Read and write
class GlobalWorker(Base):
    __tablename__ = 'workers_global'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)
    position_id = Column(Integer, ForeignKey('positions.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    insurance_id = Column(Integer, ForeignKey('insurances_global.id'))

    location = relationship('Location')
    position = relationship('Position')
    insurance = relationship('GlobalInsurance')


# Read and Write
class GlobalPosition(Base):
    __tablename__ = 'positions_global'
    # id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)


class GlobalWorkerPreference(Base):
    __tablename__ = 'workers_preferences_global'
    __table_args__ = (
        PrimaryKeyConstraint('worker_id', 'location_id'),
    )
    worker_id = Column(Integer, ForeignKey('workers_global.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))

    worker = relationship('GlobalWorker')
    location = relationship('Location')


# Read and write
class GlobalInsurance(Base):
    __tablename__ = 'insurances_global'
    id = Column(Integer, primary_key=True)
    insurer_id = Column(Integer, ForeignKey('insurers.id'))
    expiration_date = Column(Date)

    class Insurerr(Base):
        __tablename__ = 'insurers'
        id = Column(Integer, primary_key=True)
        name = Column(String)

    insurer = relationship('Insurerr')

