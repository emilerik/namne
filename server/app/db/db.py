from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL, IS_PRODUCTION
from app.db_models import DbBase

# Configure engine based on database type
if IS_PRODUCTION and DATABASE_URL.startswith("postgresql"):
    # PostgreSQL doesn't need check_same_thread
    engine = create_engine(DATABASE_URL)
else:
    # SQLite needs check_same_thread=False
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    """Drop all existing tables and create all database tables from scratch"""
    DbBase.metadata.drop_all(bind=engine)  # Drop all existing tables
    DbBase.metadata.create_all(bind=engine)  # Create all tables


def get_db():
    conn = SessionLocal()
    try:
        yield conn
    finally:
        conn.close()
