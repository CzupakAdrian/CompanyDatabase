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
    position_id = Column(Integer, ForeignKey('positions.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    insurance_id = Column(Integer, ForeignKey('insurances.id'))

    location = relationship('Location')
    position = relationship('Position')
    # insurance = relationship('Insurance') # Unccoment when fragmentation done


# Modify to vertical fragmentation
# class Insurance(Base):
#     __tablename__ = 'insurances'
#     id = Column(Integer, primary_key=True)
#     insurer_id = Column(Integer, ForeignKey('insurers.id'))
#     expiration_date = Column(Date)


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


class Insurer(Base):
    __tablename__ = 'insurers_local'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class GlobalLocation(Base):
    __tablename__ = 'locations_global'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class GlobalWorker(Base):
    __tablename__ = 'workers_global'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    birth_date = Column(Date)
    position_id = Column(Integer, ForeignKey('positions.id'))
    location_id = Column(Integer, ForeignKey('locations_global.id'))
    insurance_id = Column(Integer, ForeignKey('insurances_global.id'))

    location = relationship('GlobalLocation')
    position = relationship('Position')
    insurance = relationship('GlobalInsurance')


class PositionGlobal(Base):
    __tablename__ = 'positions_global'
    id = Column(Integer, primary_key=True)
    position = Column(String)


class GlobalWorkerPreference(Base):
    __tablename__ = 'workers_preferences_global'
    worker_id = Column(Integer, ForeignKey('workers_global.id'), primary_key=True)
    location_id = Column(Integer, ForeignKey('locations_global.id'))

    worker = relationship('GlobalWorker')
    location = relationship('GlobalLocation')


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



