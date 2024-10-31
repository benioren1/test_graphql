from graphene import ObjectType, List, Field, Int, Date, String
from data_base.db_connaction import db_session
from gql.types import CityType,MissionType
from models.cities import CityModel
from models.contries import CountryModel
from models.mission import MissionModel
from models.targets import TargetModel
from datetime import date


class Query(ObjectType):
    all_cities = List(CityType)
    all_missions = List(MissionType)
    mission_by_id = Field(MissionType,mission_id=Int())
    missions_by_range_date = List(MissionType,min_date=Date(),max_date=Date())
    missions_by_country = List(CityType,country_name=String())

    @staticmethod
    def resolve_all_cities(self, info):
        return db_session.query(CityModel).join(CountryModel).all()

    @staticmethod
    def resolve_all_missions(self, info):
        return db_session.query(MissionModel).all()

    @staticmethod
    def resolve_mission_by_id(self,info,mission_id):
        mission = db_session.query(MissionModel).all(mission_id)
        return mission

    @staticmethod
    def resolve_missions_by_range_date(self,info,min_date,max_date):
        return db_session.query(MissionModel).filter(MissionModel.mission_date.between(min_date,max_date)).all()

    def resolve_missions_by_country(self,info,country_name):
        pass


    






