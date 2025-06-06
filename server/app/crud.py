from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .db_models import DbNameEntry, DbUser, DbVote
from .schema import NameEntry, NameId, User, Username, Vote, VoteId


def get_names(username: str, db_session: Session) -> list[NameEntry]:
    stmt = (
        select(DbNameEntry)
        .where(
            ~select(DbVote)
            .where(DbVote.name_id == DbNameEntry.id)
            .where(DbVote.username == username)
            .exists()
        )
        .order_by(func.random())
        .limit(100)
    )
    result = db_session.execute(stmt)
    names = list(result.scalars().all())
    return [
        NameEntry(id=NameId(entry.id), name=entry.name, gender=entry.gender)
        for entry in names
    ]


def vote_on_name(
    db_session: Session, name_id: NameId, username: Username, vote: Vote
) -> User | None:

    assert isinstance(
        vote, Vote
    ), f"Can only vote like, dislike, or superlike, not {vote=}"

    # Get other person's vote
    get_stmt = select(DbVote).where(DbVote.name_id == name_id)
    result = db_session.execute(get_stmt)
    curr_votes = result.scalars().all()

    other_person_vote: Vote | None = None
    other_person = None
    for existing_vote in curr_votes:
        if existing_vote.username == username:
            raise HTTPException(403, "User has already voted")
        # The other person has voted
        other_person_res = db_session.execute(
            select(DbUser).where(DbUser.username == existing_vote.username)
        )
        other_person = other_person_res.scalar_one_or_none()
        assert other_person is not None

        other_person_vote = Vote(existing_vote.vote)

    try:
        print(f"Inserting vote... {name_id=}, {username=}, {vote=}")
        new_vote = DbVote(
            id=VoteId(str(uuid4())), username=username, name_id=name_id, vote=vote.value
        )
        print(f"new vote id is {new_vote.id}")
        db_session.add(new_vote)
        db_session.commit()
    except Exception as e:
        print(f"Error: couldn't insert vote, {e=}")
        raise HTTPException(400, f"Error: could not insert vote, {e=}")

    is_match = (
        other_person_vote is not None and other_person_vote.value > 0 and vote.value > 0
    )

    return (
        User(username=Username(other_person.username), name=other_person.name)
        if is_match and other_person
        else None
    )

    # Check if the other one has voted too
