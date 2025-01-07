from flask_restful import fields
from app.serializers.products import product_for_order_fields

order_fields = {
    "user_id": fields.String,
    "product_id": fields.String,
    "quantity": fields.Integer,
}
order_item_fields = {
    "id": fields.String,
    "quantity": fields.Integer,
    "consumed_count": fields.Integer,
    "product": fields.Nested(product_for_order_fields),
}
orders_paginated_fields = {
    "total": fields.Integer,
    "pages": fields.Integer,
    "current_page": fields.Integer,
    "per_page": fields.Integer,
    "data": fields.List(fields.Nested(order_item_fields)),
}
