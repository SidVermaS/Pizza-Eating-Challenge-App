from app.config import db
import uuid
from sqlalchemy import func


class ConsumedLogs(db.Model):
    __tablename__ = "consumed_logs"
    # __table_args__ = {
    #   "schema":"challenge"
    # }
    id = db.Column(
        db.String(36), primary_key=True, default=lambda: str(uuid.uuid4), nullable=False
    )
    consumed_count = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    product_id = db.Column(db.String(36), db.ForeignKey("products.id"))
    order_id = db.Column(db.String(36), db.ForeignKey("orders.id"))
    created_at = db.Column(db.DateTime, default=func.now())

    product = db.relationship("Products", backref="consumed_logs", lazy=True)
    order = db.relationship("Orders", backref="consumed_logs", lazy=True)
    user = db.relationship("Uusers", backref="consumed_logs", lazy=True)

    def __repr__(self):
        return f"<ConsumedLogs user_id: {self.user_id} order_id: {self.order_id}>"
