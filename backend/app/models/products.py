from app.config import db
import uuid


class Products(db.Model):
    __tablename__ = "products"
    # __table_args__ = {"schema":"product"}
    id = db.Column(
        db.String(36), primary_key=True, default=lambda: str(uuid.uuid4), nullable=False
    )
    title = db.Column(db.String(100), nullable=False, unique=True)
    imagePath = db.Column(db.String(200), nullable=False)
    rate = db.Column(db.Integer, nullable=False)

    # Relationships
    order = db.relationship(
        "Orders", back_populates="product", lazy=True, cascade="all, delete-orphan"
    )
    consumed_log = db.relationship(
        "ConsumedLogs",
        back_populates="product",
        lazy=True,
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Products {self.title}>"
