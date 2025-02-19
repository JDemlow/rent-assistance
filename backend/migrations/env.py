import os
from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from dotenv import load_dotenv
from urllib.parse import unquote

# Load environment variables
load_dotenv()

# Get the database URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is missing from .env file")

# Decode special characters (like %23 for #)
DATABASE_URL = unquote(DATABASE_URL)

# Import models for migrations
from models import Base

# Alembic Config object
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set target metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = create_async_engine(DATABASE_URL, poolclass=pool.NullPool)

    async def do_migrations():
        async with connectable.begin() as connection:
            await connection.run_sync(
                lambda conn: context.configure(
                    connection=conn, target_metadata=target_metadata
                )
            )
            await connection.run_sync(lambda _: context.run_migrations())

    import asyncio

    asyncio.run(do_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
