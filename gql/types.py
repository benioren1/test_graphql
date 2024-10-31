import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from datetime import datetime, date
from data_base.db_connaction import db_session
from models.cities import CityModel
from models.contries import CountryModel
from models.targets import TargetModel
from models.mission import MissionModel
from models.targettypes import TargetTypeModel


class CityType(SQLAlchemyObjectType):
    class Meta:
        model = CityModel
        interfaces = (graphene.relay.Node,)


class CountryType(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (graphene.relay.Node,)

class MissionType(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (graphene.relay.Node,)


class TargetType(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (graphene.relay.Node,)

class TargetTypeType(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypeModel
        interfaces = (graphene.relay.Node,)