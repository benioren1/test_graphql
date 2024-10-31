from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey, Index, Numeric
from sqlalchemy.orm import relationship

from data_base.db_connaction import Base

class TargetTypeModel(Base):
    __tablename__ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)

