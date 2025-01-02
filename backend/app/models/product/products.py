import uuid

from ...config import db

class Products(db.Model):
  __table__name = "products"
  __table__args = {"schema":"product"}
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4), nullable=False)
  title = db.Column(db.String(100), nullable = False, unique = True)
  rate = db.Column(db.Integer, nullable = False)
  
   # Relationships
  orders = db.relationship("orders", backref = "product.products", lazy = True, cascade = "all, delete-orphan")
  consumedLogs = db.relationship("consumed_logs", backref="product.products", lazy=True, cascade = "all, delete-orphan")
  
  def __repr__(self):
    return f"<Products {self.title}>"