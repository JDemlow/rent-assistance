import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from dotenv import load_dotenv

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL is not set in .env")

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)


async def test_db_connection():
    """Simple function to test the database connection."""
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))  # ✅ FIXED: text() added
        print("✅ Database connection successful:", result.fetchall())


if __name__ == "__main__":
    asyncio.run(test_db_connection())
