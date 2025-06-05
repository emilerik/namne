from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DATABASE_URL
from app.db_models import DbBase


engine = create_engine(DATABASE_URL)

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
