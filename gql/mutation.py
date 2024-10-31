from graphene import Mutation, String, Boolean, Field, Int, Date
from sqlalchemy import Numeric

from data_base.db_connaction import db_session
from gql.types import MissionType
from models.mission import MissionModel


class AddMission(Mutation):
    class Arguments:
        mission_date = Date(required=True)
        airborne_aircraft = Numeric(10, 2)
        attacking_aircraft = Numeric(10, 2)
        bombing_aircraft =Numeric(10, 2)
        aircraft_returned = Numeric(10, 2)
        aircraft_failed = Numeric(10, 2)
        aircraft_damaged = Numeric(10, 2)
        aircraft_lost = Numeric(10, 2)

    success = Boolean()
    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info,mission_date, airborne_aircraft, attacking_aircraft,bombing_aircraft, aircraft_returned, aircraft_damaged
                , aircraft_lost):
        with db_session() as session:
            inserted_mission = MissionModel(mission_date=mission_date, airborne_aircraft =airborne_aircraft,
                                             attacking_aircraft =attacking_aircraft,bombing_aircraft=bombing_aircraft,
                                             aircraft_returned =aircraft_returned,aircraft_failed=aircraft_returned,
                                             aircraft_damaged=aircraft_damaged,
                                             aircraft_lost=aircraft_lost
                                            )
            session.add(inserted_mission)
            session.commit()
            session.refresh(inserted_mission)
            return AddEmployee(success=True, mission=inserted_mission)


class AddEmployee(Mutation):
    class Arguments:
        name = String(required=True)
        email = String(required=True)

    success = Boolean()
    employee = Field(EmployeeType)

    @staticmethod
    def mutate(root, info, name, email):
        with session_maker() as session:
            inserted_employee = Employee(name=name, email=email)
            session.add(inserted_employee)
            session.commit()
            session.refresh(inserted_employee)
            return AddEmployee(success=True, employee=inserted_employee)