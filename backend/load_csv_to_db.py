import pandas as pd
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

DATABASE_URL = "postgresql+asyncpg://postgres:your_password@localhost:5432/denver_rent"
engine = create_async_engine(DATABASE_URL, echo=True)


async def load_csv():
    df = pd.read_csv("denver_data.csv")
    async with engine.begin() as conn:
        await conn.run_sync(df.to_sql, "rent_data", if_exists="replace", index=False)
    print("✅ Data successfully loaded into PostgreSQL!")


asyncio.run(load_csv())
