import os

# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# Environment
ENV = os.getenv("ENV", "development")
IS_PRODUCTION = ENV == "production"

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "")

# CORS settings
CORS_ORIGINS = os.getenv(
    "CORS_ORIGINS", "http://localhost:5173,https://localhost:5173"
).split(",")

# Server settings
# HOST = os.getenv("HOST", "0.0.0.0")
# PORT = int(os.getenv("PORT", 8000))
