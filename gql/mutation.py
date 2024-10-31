from graphene import Mutation, String, Boolean, Field, Int, Date, ObjectType, Float
from sqlalchemy import Numeric

from data_base.db_connaction import db_session
from gql.types import MissionType, TargetType
from models.mission import MissionModel
from models.targets import TargetModel


class AddMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)
        mission_date = Date(required=True)
        airborne_aircraft =Float()
        attacking_aircraft = Float()
        bombing_aircraft =Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    success = Boolean()
    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info,mission_id,mission_date, airborne_aircraft, attacking_aircraft,bombing_aircraft,aircraft_failed, aircraft_returned, aircraft_damaged
                , aircraft_lost):
        with db_session() as session:
            inserted_mission = MissionModel(mission_id=mission_id,mission_date=mission_date, airborne_aircraft =airborne_aircraft,
                                             attacking_aircraft =attacking_aircraft,bombing_aircraft=bombing_aircraft,
                                             aircraft_returned =aircraft_returned,aircraft_failed=aircraft_failed,
                                             aircraft_damaged=aircraft_damaged,
                                             aircraft_lost=aircraft_lost
                                            )
            session.add(inserted_mission)
            session.commit()
            session.refresh(inserted_mission)
            return AddMission(success=True, mission=inserted_mission)


class AddTarget(Mutation):
    class Arguments:
        target_id = Int(required=True)
        mission_id = Int(required=True)
        # mission = relationship("MissionModel", back_populates="target")
        target_industry = String()
        city_id = Int(required=True)
        # city = relationship("CityModel", back_populates="target")
        target_type_id = Int()
        target_priority = Int()
    success = Boolean()
    mission = Field(TargetType)

    @staticmethod
    def mutate(root, info,target_id,mission_id,target_industry,city_id,target_type_id,target_priority ):
        with db_session() as session:
            inserted_Target = TargetModel(target_id=target_id,mission_id=mission_id,target_industry=target_industry,city_id=city_id,
                                          target_type_id=target_type_id,target_priority=target_priority
                                            )
            session.add(inserted_Target)
            session.commit()
            session.refresh(inserted_Target)
            return AddMission(success=True, mission=inserted_Target)
class UpdateMission(Mutation):
    class Arguments:
        id = Int(required=True)
        aircraft_lost = Float()
        aircraft_damaged = Float()
        aircraft_failed = Float()
        aircraft_returned = Float()

    success = Boolean()
    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info,id, aircraft_lost, aircraft_damaged, aircraft_failed,aircraft_returned):
        with db_session() as session:
            updated_mission = session.query(MissionModel).get(id)
            updated_mission.aircraft_lost = aircraft_lost
            updated_mission.aircraft_damaged = aircraft_damaged
            updated_mission.aircraft_failed = aircraft_failed
            updated_mission.aircraft_returned = aircraft_returned

            session.commit()
            session.refresh(updated_mission)
            return UpdateMission(success=True, mission=updated_mission)

class DeleteMission(Mutation):
    class Arguments:
        user_id =Int(required=True)

    success =Boolean()

    def mutate(self, info, user_id):
        user = db_session.query(MissionModel).get(user_id)
        if not user:
            return DeleteMission(success=False)
        db_session.delete(user)
        db_session.commit()
        return DeleteMission(success=True)





class Mutation(ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()
    update_mission = UpdateMission.Field()
    delete_mission = DeleteMission.Field()