import os
from fastapi import FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# FastAPI instance
app = FastAPI()

# Database connection using .env
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


# Rent Data Model
class RentData(Base):
    __tablename__ = "rent_data"
    id = Column(Integer, primary_key=True, index=True)
    neighborhood = Column(String, nullable=False)
    median_rent = Column(Float, nullable=False)
    year = Column(Integer, nullable=False)


# FastAPI Route to Fetch Rent Data
@app.get("/rent-data")
async def get_rent_data():
    async with AsyncSessionLocal() as session:
        try:
            query = select(RentData).limit(10)
            result = await session.execute(query)
            rows = result.scalars().all()
            if not rows:
                raise HTTPException(status_code=404, detail="No rent data found")
            return {"data": [row.__dict__ for row in rows]}
        except Exception as e:
            print(f"Database Error: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")
