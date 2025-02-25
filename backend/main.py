from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models import SessionLocal, RentData  # ✅ Absolute Import
from backend.schemas import RentDataSchema  # ✅ Absolute Import
from typing import List

app = FastAPI(
    title="Denver Rent & Housing Insights API",
    description="A FastAPI backend for retrieving and analyzing Denver rent trends.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency to get a database session
async def get_db():
    async with SessionLocal() as session:
        yield session


# ✅ Updated API Route: Fetch All Rent Data using `RentDataSchema`
@app.get("/rent_data/", response_model=List[RentDataSchema])
async def get_rent_data(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(RentData))
    rent_data = result.scalars().all()
    return [
        RentDataSchema.model_validate(row) for row in rent_data
    ]  # ✅ Convert SQLAlchemy models to Pydantic
