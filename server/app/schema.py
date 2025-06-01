from enum import IntEnum
from typing import NewType

from pydantic import BaseModel, Field

Username = NewType("Username", str)
VoteId = NewType("VoteId", str)
NameId = NewType("NameId", str)


class Vote(IntEnum):
    DISLIKE = 0
    LIKE = 1
    SUPERLIKE = 2


class NameEntry(BaseModel):
    id: NameId
    name: str
    gender: str


class VoteOnNameRequest(BaseModel):
    vote: int


class GetNamesResponse(BaseModel):
    names: list[NameEntry]


class User(BaseModel):
    username: Username
    name: str


class VoteOnNameResponse(BaseModel):
    matched_with: User | None = Field(None, alias="matchedWith")
