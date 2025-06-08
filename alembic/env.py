import os
import sys

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from cp_lib.db import Base  # your declarative base

# Alembic Config object for accessing .ini file values
config = context.config

# Set up logging
fileConfig(config.config_file_name)

# Set the database URL from the environment variable
db_url = os.getenv("CHRONOS_DB_URL")
if db_url:
    config.set_main_option("sqlalchemy.url", db_url)

# Metadata for migrations
target_metadata = Base.metadata

# Override sqlalchemy.url from environment variable if set
config.set_main_option(
    "sqlalchemy.url",
    os.getenv("CHRONOS_DB_URL", config.get_main_option("sqlalchemy.url"))
)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,  # detect type changes
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # detect type changes
        )

        with context.begin_transaction():
            context.run_migrations()


# Execute migrations based on the mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
