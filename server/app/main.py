import logging

from fastapi import Body, Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from app.auth import authenticate
from app.config import CORS_ORIGINS
from app.crud import get_names, vote_on_name
from app.db.db import create_tables, get_db
from app.schema import (
    GetNamesResponse,
    NameId,
    Username,
    Vote,
    VoteOnNameRequest,
    VoteOnNameResponse,
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Name Voting API", version="1.0.0")

# TODO
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_root():
    return {"message": "Name Voting API", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"}


@app.post("/admin/init-db")
async def init_database_endpoint():
    """Manual database initialization endpoint (for troubleshooting)"""
    try:
        logger.info("Manual database initialization requested")

        # Create tables
        create_tables()
        logger.info("Tables created successfully")

        # Initialize users
        from app.init_users import init_users

        init_users(interactive=False)
        logger.info("Users initialized successfully")

        return {"message": "Database initialized successfully", "status": "success"}

    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise HTTPException(
            status_code=500, detail=f"Database initialization failed: {str(e)}"
        )


@app.get("/names", dependencies=[Depends(authenticate)])
async def get_names_endpoint(
    db_session: Session = Depends(get_db), username: str = Depends(authenticate)
) -> GetNamesResponse:
    logger.info(f"Getting names for user: {username}")
    names = get_names(username, db_session)
    return GetNamesResponse(names=names)


@app.post("/name/{name_id}", dependencies=[Depends(authenticate)])
async def vote_on_name_endpoint(
    name_id: NameId,
    db_session: Session = Depends(get_db),
    body: VoteOnNameRequest = Body(...),
    username: Username = Depends(authenticate),
) -> VoteOnNameResponse:
    try:
        vote = Vote(body.vote)
    except:
        raise ValueError(f"Value needs to be {Vote._member_map_=}")

    logger.info(f"User {username} voting {vote} on name {name_id}")
    matched_with = vote_on_name(db_session, name_id, username, vote)
    return VoteOnNameResponse(matchedWith=matched_with)


@app.get("/authenticate", dependencies=[Depends(authenticate)])
def read_private(username: str = Depends(authenticate)):
    return {"message": f"Hello, {username}!"}
