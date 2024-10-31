from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index, Numeric
from sqlalchemy.orm import relationship

from data_base.db_connaction import Base

class CityModel(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer,primary_key=True)
    city_name = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    country_id = Column(Integer,ForeignKey('countries.country_id'))
    country = relationship("CountryModel", back_populates="cities")
    target = relationship("TargetModel", back_populates="city")
