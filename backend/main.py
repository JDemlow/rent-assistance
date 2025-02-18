from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import AsyncSessionLocal
from models import RentData  # Make sure RentData model exists

app = FastAPI()


# Dependency to get the database session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# Simple API route to get rent data
@app.get("/rent-data")
async def get_rent_data(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(RentData).limit(10))  # Fetch 10 records
    rent_data = result.scalars().all()
    return {
        "data": [row.__dict__ for row in rent_data]
    }  # Convert ORM objects to dictionaries
