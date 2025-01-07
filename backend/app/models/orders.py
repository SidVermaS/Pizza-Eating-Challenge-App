from app.config import db

import uuid
from sqlalchemy import func


class Orders(db.Model):
    __tablename__ = "orders"
    # __table_args__ = {"schema":"order"}
    id = db.Column(
        db.String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        nullable=False,
    )
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"))
    product_id = db.Column(db.String(36), db.ForeignKey("products.id"))
    quantity = db.Column(db.Integer, nullable=False, default=0)
    consumed_count = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, default=func.now())

    # Relationships
    consumed_log = db.relationship(
        "ConsumedLogs", back_populates="order", lazy=True, cascade="all, delete-orphan"
    )
    product = db.relationship(
        "Products",
        back_populates="order",
        lazy=True,
    )
    user = db.relationship(
        "Users",
        back_populates="order",
        lazy=True,
    )

    def __repr__(self):
        return f"<Orders product_id: {self.product_id} user_id: {self.user_id} quantity: {self.quantity}>"
