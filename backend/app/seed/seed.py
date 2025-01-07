import os
import json

from app.config import db
from app.models import Users, Products, Orders, ConsumedLogs


class SeedInfo:
    def __init__(self, model, file_name):
        self.model = model
        self.file_name = file_name


# Helper function to read JSON data from a file
def read_json_files(file_name):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data", file_name)
    with open(file_path, "r") as file:
        return json.load(file)


def seedUsers():
    data = read_json_files("users.data.json")
    # users = [Users(user.id,) for user in data]
    users = [
        Users(
            id=user["id"],
            name=user["name"],
            age=user["age"],
            gender=user["gender"],
            coins=user["coins"],
            consumed_count=user["consumed_count"],
            orders=[],
        )
        for user in data
    ]
    db.session.add_all(users)


def run_seed():
    try:
        all_seed_info = [
            SeedInfo(Users, "users.data.json"),
            SeedInfo(Products, "products.data.json"),
            SeedInfo(Orders, "orders.data.json"),
            SeedInfo(ConsumedLogs, "consumed_logs.data.json"),
        ]

        with db.session.begin():
            for seed_info in all_seed_info:
                data = read_json_files(seed_info.file_name)
                db.session.add_all(seed_info.model(**item) for item in data)
            db.session.commit()
            print("Data seeded successfully")
    except Exception as e:
        db.session.rollback()
        print(f"e: {e}")


# def run_seed(app):
#   with app.app_context():
#     try:
#       db.session.begin_nested()

#       seedUsers()
#       db.session.commit()
#     except Exception as e:
#       print(f"e: {e}")
#       db.session.rollback()
#     finally:
#       db.session.close()
