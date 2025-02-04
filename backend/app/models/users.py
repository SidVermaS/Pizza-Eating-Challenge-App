from app.config import db
from app.consts import GenderE

import uuid
from sqlalchemy import Enum


class Users(db.Model):
    __tablename__ = "users"
    # __table_args__ = {"schema":"user"}
    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False,
    )
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(Enum(GenderE), nullable=False)
    coins = db.Column(db.Integer, nullable=False, default=500)
    consumed_count = db.Column(db.Integer, nullable=False, default=0)
    rank = db.Column(db.Integer, nullable=False)

    # Relationships
    order = db.relationship(
        "Orders", back_populates="user", lazy=True, cascade="all, delete-orphan"
    )
    consumed_log = db.relationship(
        "ConsumedLogs", back_populates="user", lazy=True, cascade="all, delete-orphan"
    )

    # def to_dict(self):
    #   return { 'id': self.id, 'name': self.name, 'age': self.age }
    def __repr__(self):
        return f"<Users {self.name}>"
