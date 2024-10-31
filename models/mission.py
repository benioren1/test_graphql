from graphene import Float
from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index, Numeric
from sqlalchemy.orm import relationship

from data_base.db_connaction import Base

class MissionModel(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date,nullable=False)
    airborne_aircraft = Column(Numeric(10,2),nullable=True)
    attacking_aircraft =Column(Numeric(10,2),nullable=True)
    bombing_aircraft =Column(Numeric(10,2),nullable=True)
    aircraft_returned = Column(Numeric(10,2),nullable=True)
    aircraft_failed =Column(Numeric(10,2),nullable=True)
    aircraft_damaged =Column(Numeric(10,2),nullable=True)
    aircraft_lost =Column(Numeric(10,2),nullable=True)
    # target_id = Column(Integer, ForeignKey('targets.target_id'))
    target = relationship("TargetModel", back_populates="mission")


