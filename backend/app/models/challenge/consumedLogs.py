import uuid
from sqlalchemy import func

from ...config import db

class ConsumedLogs(db.Model):
  __table__name = "consumed_logs"
  __table__args = {
    "schema":"challenge"
  }
  id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4), nullable=False)
  user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
  product_id = db.Column(db.String(36), db.ForeignKey("products.id"))
  order_id = db.Column(db.String(36), db.ForeignKey("orders.id"))
  created_at = db.Column(db.DateTime, default = func.now())  
  
  def __repr__(self):
    return f"<ConsumedLogs user_id: {self.user_id} order_id: {self.order_id}>"