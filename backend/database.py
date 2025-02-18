import os
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import text
from dotenv import load_dotenv

# ✅ Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# ✅ Retrieve DATABASE_URL
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set in .env")

# ✅ Create Async Engine
engine = create_async_engine(DATABASE_URL, echo=True)

# ✅ Create Async Session Factory
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# ✅ Define Base Model
Base = declarative_base()


# ✅ Test Database Connection
async def test_db_connection():
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        print("✅ Database connection successful:", result.fetchall())


# Run the test when executing this script
if __name__ == "__main__":
    asyncio.run(test_db_connection())
