"""
Script to initialize users in the database
Usage: python -m app.init_users
"""

import sys

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db_models import DbUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Default users to create
DEFAULT_USERS = [
    {"username": "emil", "name": "Emil", "password": "950615"},
    {"username": "agnes", "name": "Agnes", "password": "940708"},
]


def create_user(db: Session, username: str, name: str, password: str):
    """Create a user with hashed password"""
    hashed_password = pwd_context.hash(password)
    user = DbUser(username=username, name=name, password=hashed_password)
    db.add(user)
    return user


def init_users(interactive: bool = True) -> None:
    """Initialize default users"""
    db = next(get_db())

    try:
        # Check if users already exist
        existing_users = db.query(DbUser).all()
        if existing_users:
            print(f"Users already exist: {[u.username for u in existing_users]}")

            if interactive:
                response = input("Do you want to recreate all users? (y/N): ")
                if response.lower() != "y":
                    return
            else:
                # In non-interactive mode, skip if users exist
                print("Skipping user initialization (non-interactive mode)")
                return

            # Delete existing users
            db.query(DbUser).delete()
            db.commit()
            print("Deleted existing users")

        # Create default users
        for user_data in DEFAULT_USERS:
            user = create_user(
                db,
                username=user_data["username"],
                name=user_data["name"],
                password=user_data["password"],
            )
            print(f"Created user: {user.username}")

        db.commit()
        print("Successfully initialized users!")

    except Exception as e:
        print(f"Error initializing users: {e}")
        db.rollback()
        if interactive:
            sys.exit(1)
        else:
            raise
    finally:
        db.close()


if __name__ == "__main__":
    init_users(interactive=True)
