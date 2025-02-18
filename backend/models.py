from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class RentData(Base):
    __tablename__ = "rent_data"

    OBJECTID = Column(Integer, primary_key=True)
    NBHD_NAME = Column(String, nullable=False)
    NBHD_ID = Column(Integer)
    DIST_NUM = Column(Integer)
    Pct_OccupiedUnitsWithRenters = Column(Float)
    Pct_HouseholdsCostBurdened = Column(Float)
    Pct_PopulationInPoverty = Column(Float)
    Pct_PopulationMinority = Column(Float)
