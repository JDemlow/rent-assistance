from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
import os
from dotenv import load_dotenv

# ✅ Explicitly load .env file from backend directory
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# ✅ Load database URL from .env file
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")

# ✅ Create an async database engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# ✅ Create a session factory
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

# ✅ Define a Base class for models
Base = declarative_base()


# ✅ Define RentData table
class RentData(Base):
    __tablename__ = "rent_data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    neighborhood = Column(String, nullable=False, index=True)
    rent_price = Column(Integer, nullable=False)
