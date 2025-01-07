from app.serializers.common import EnumField
from app.consts.user import GenderE
from flask_restful import fields

user_fields = {
    "id": fields.String,
    "name": fields.String,
    "age": fields.Integer,
    "gender": EnumField(GenderE),
    "coins": fields.Integer,
    "rank": fields.Integer,
    "consumed_count": fields.Integer,
}
user_paginated_fields = {
    "total": fields.Integer,
    "pages": fields.Integer,
    "current_page": fields.Integer,
    "per_page": fields.Integer,
    "data": fields.List(fields.Nested(user_fields)),
}
