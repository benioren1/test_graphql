from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index, Numeric
from sqlalchemy.orm import relationship

from data_base.db_connaction import Base

class TargetModel(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))
    mission = relationship("MissionModel", back_populates="target")
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    city = relationship("CityModel", back_populates="target")
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)

