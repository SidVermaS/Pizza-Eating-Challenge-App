import uuid
from sqlalchemy import Enum

from config import db
from consts import Gender

class User(db.Model):
  __table__name = "users"
  __table__args = {"schema":"user"}
  id = db.Column(db.String(36), primary_key = True, default = lambda: str(uuid.uuid4()), nullable = False)
  name = db.Column(db.String(100), nullable = False)
  age = db.Column(db.Integer, nullable = False)
  gender = db.Column(Enum(Gender), nullable = False)
  coins = db.Column(db.Integer, nullable = False, default = 500)
  
  def __repr__(self):
    return f"<User {self.name}>"