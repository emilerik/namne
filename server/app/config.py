import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Environment
ENV = os.getenv("ENV", "development")
IS_PRODUCTION = ENV == "production"

# Database
_db_url = ""
if IS_PRODUCTION:
    # In production, use PostgreSQL from Render
    _db_url = os.getenv("DATABASE_URL", "")
    if _db_url:
        # Convert postgres:// to postgresql:// for SQLAlchemy compatibility
        _db_url = _db_url.replace("postgres://", "postgresql://")
else:
    # In development, use local SQLite
    _database_path = str(BASE_DIR / "app" / "db" / "app.db")
    _db_url = f"sqlite:///{_database_path}"

DATABASE_URL = _db_url

# CORS settings
CORS_ORIGINS = os.getenv(
    "CORS_ORIGINS", "http://localhost:5173,https://localhost:5173"
).split(",")

# Authentication
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Server settings
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
