from graphene import ObjectType, List, Field, Int, Date, String
from data_base.db_connaction import db_session
from gql.types import CityType, MissionType
from models.cities import CityModel
from models.contries import CountryModel
from models.mission import MissionModel
from models.targets import TargetModel
from datetime import date


class Query(ObjectType):
    all_cities = List(CityType)
    all_missions = List(MissionType)
    mission_by_id = Field(MissionType, mission_id=Int())
    missions_by_range_date = List(MissionType, min_date=Date(), max_date=Date())
    missions_by_country = List(MissionType, country_name=String())
    missions_by_target_Industry = List(MissionType, target_industry=String())
    aircraft_by_mission = Field(String,mission_id=Int())


    @staticmethod
    def resolve_all_cities(self, info):
        return db_session.query(CityModel).join(CountryModel).all()

    @staticmethod
    def resolve_all_missions(self, info):
        return db_session.query(MissionModel).all()

    @staticmethod
    def resolve_mission_by_id(self, info, mission_id):
        mission = db_session.query(MissionModel).get(mission_id)
        return mission

    @staticmethod
    def resolve_missions_by_range_date(self, info, min_date, max_date):
        return db_session.query(MissionModel).filter(MissionModel.mission_date.between(min_date, max_date)).all()

    def resolve_missions_by_country(self, info, country_name):
        country = db_session.query(CountryModel).filter(CountryModel.country_name==country_name).first()
        missions = db_session.query(MissionModel).join(TargetModel).join(CityModel).filter(CityModel.country_id == country.country_id).all()
        return missions

    def resolve_missions_by_target_Industry(self, info, target_industry):
        return db_session.query(MissionModel).join(TargetModel).filter(
            TargetModel.target_industry == target_industry).all()
    def resolve_missions_by_city(self, info, mission_id):
        new_mission = db_session.query(MissionModel).get(mission_id)
        return f"airborne_aircraft: {new_mission.airborne_aircraft}, attacking_aircraft: {new_mission.attacking_aircraft}, bombing_aircraft: {new_mission.bombing_aircraft}"



