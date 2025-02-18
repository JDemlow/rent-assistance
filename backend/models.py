from sqlalchemy import Column, String, BigInteger, Float
from database import Base


class RentData(Base):
    __tablename__ = "rent_data"

    OBJECTID = Column(BigInteger, primary_key=True, index=True)
    NBHD_NAME = Column(String)
    Pct_OccupiedUnitsWithRenters = Column(Float)
    Pct_HouseholdsCostBurdened = Column(Float)
    Pct_PopulationInPoverty = Column(Float)
    Nmbr_PerCapitaIncome = Column(BigInteger)
