import uuid
from sqlalchemy import Enum

from ...config import db
from ...consts import Gender

class Users(db.Model):
  __table__name = "users"
  __table__args = {"schema":"user"}
  id = db.Column(db.String(36), primary_key = True, default = lambda: str(uuid.uuid4()), nullable = False)
  name = db.Column(db.String(100), nullable = False)
  age = db.Column(db.Integer, nullable = False)
  gender = db.Column(Enum(Gender), nullable = False)
  coins = db.Column(db.Integer, nullable = False, default = 500)
  consumed_count = db.Column(db.Integer, nullable = False, default = 0)
  
  # Relationships
  orders = db.relationship("orders", backref = "user.users", lazy = True, cascade = "all, delete-orphan")
  consumedLogs = db.relationship("consumed_logs", backref="user.users", lazy=True, cascade = "all, delete-orphan")
  
  def __repr__(self):
    return f"<Users {self.name}>"