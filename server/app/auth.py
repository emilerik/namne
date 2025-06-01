from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.db.db import get_db
from app.db_models import DbUser

security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate(
    credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)
):
    """Authenticate user against database"""
    user = db.query(DbUser).filter(DbUser.username == credentials.username).first()

    if not user or not pwd_context.verify(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username
