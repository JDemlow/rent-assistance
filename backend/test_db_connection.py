import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
import os

# Use the same DATABASE_URL from database.py
DATABASE_URL = os.getenv("DATABASE_URL")


async def test_connection():
    try:
        engine = create_async_engine(DATABASE_URL, echo=True)
        async with engine.begin() as conn:
            result = await conn.execute("SELECT version();")
            version = result.scalar()
            print(f"✅ Connected to PostgreSQL: {version}")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")


asyncio.run(test_connection())
