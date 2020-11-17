from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base


class Insurance(declarative_base()):
    __tablename__ = 'insurances_global'
    id = Column(Integer, primary_key=True)
    insurer_id = Column(Integer)
    expiration_date = Column(Date)

    def __repr__(self):
        return "<Insurance(id='%d', insurer_id='%d', expiration_date='%s')>" %\
               (self.id, self.insurer_id, self.expiration_date)