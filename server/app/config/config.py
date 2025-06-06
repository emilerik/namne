import os

from dotenv import load_dotenv

# # Load environment variables from .env file
load_dotenv(
    dotenv_path=".env.development",
    override=True,
)

# Environment
ENV = os.getenv("ENV", "development")
IS_PRODUCTION = ENV == "production"

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "")

# CORS settings
CORS_ORIGINS = os.getenv(
    "CORS_ORIGINS", "http://localhost:5173,https://localhost:5173"
).split(",")
