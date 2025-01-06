import uuid

from ..config import db

class Products(db.Model):
  __tablename__ = "products"
  # __table_args__ = {"schema":"product"}
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4), nullable=False)
  title = db.Column(db.String(100), nullable = False, unique = True)
  imagePath = db.Column(db.String(200), nullable = False)
  rate = db.Column(db.Integer, nullable = False)
  
   # Relationships
  orders = db.relationship("Orders", backref = "products", lazy = True, cascade = "all, delete-orphan")
  consumedLogs = db.relationship("ConsumedLogs", backref="products", lazy=True, cascade = "all, delete-orphan")
  
  def __repr__(self):
    return f"<Products {self.title}>"