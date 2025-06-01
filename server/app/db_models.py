import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class DbBase(DeclarativeBase):
    """
    Base class for all database models.
    Main job is inheriting from DeclarativeBase, but also adds utility functions
    """


class DbNameEntry(DbBase):
    __tablename__ = "name_entry"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    gender: Mapped[str]


class DbUser(DbBase):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]
    password: Mapped[str]


class DbVote(DbBase):
    __tablename__ = "vote"

    id: Mapped[str] = mapped_column(primary_key=True)
    name_id: Mapped[str] = mapped_column(ForeignKey("name_entry.id"))
    username: Mapped[str] = mapped_column(ForeignKey("user.username"))
    vote: Mapped[int]  # 0: dislike, 1: like, 2: superlike
    created_at: Mapped[str] = mapped_column(default=datetime.datetime.now(datetime.UTC))
