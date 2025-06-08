from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the database URL with a default value
DATABASE_URL = os.getenv(
    "CHRONOS_DB_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/chronos"
)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Create a base class for declarative models
Base = declarative_base()
