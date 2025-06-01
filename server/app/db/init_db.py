import csv

from sqlalchemy import insert

from app.db.db import SessionLocal, create_tables
from app.db_models import DbNameEntry, DbUser

if __name__ == "__main__":
    print("Creating database tables...")
    create_tables()

    db_session = SessionLocal()

    def seed_users():
        add_users_stmt = insert(DbUser).values(
            [
                {"username": "agnes", "name": "Agnes", "password": "1234"},
                {"username": "emil", "name": "Emil", "password": "1234"},
            ]
        )
        db_session.execute(add_users_stmt)
        db_session.commit()

    def seed_names():
        for file_path, gender in [
            ("server/app/db/data/boys_name_1000.csv", "boy"),
            ("server/app/db/data/girls_name_1000.csv", "girl"),
        ]:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                entries = [
                    {"id": row[0], "name": row[1], "gender": gender} for row in reader
                ]

            add_names_stmt = insert(DbNameEntry).values(entries)
            db_session.execute(add_names_stmt)
            db_session.commit()

    print("Seeding users...")
    seed_users()
    print("Finished seeding users.")

    print("Seeding names...")
    seed_names()
    print("Finished seeding names.")
