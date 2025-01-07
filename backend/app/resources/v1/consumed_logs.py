from app.parsers.common import get_pagination_parser
from app.services.consumed_logs_service import get_consumed_logs, save_consumed_logs
from app.consts.api import HttpStatus
from app.serializers.consumed_logs import (
    consumed_logs_item_fields,
    consumed_logs_paginated_fields,
)
from app.parsers.consumed_logs import get_consumed_logs_parser
from flask_restful import Resource, marshal_with


class ConsumedLogsByUserIdResource(Resource):
    @marshal_with(consumed_logs_paginated_fields)
    def get(self, user_id):
        pagination_parser = get_pagination_parser()
        args = pagination_parser.parse_args()
        consumed_logs = get_consumed_logs(
            user_id=user_id, page=args["page"], per_page=args["per_page"]
        )
        return consumed_logs, HttpStatus.OK.value


class ConsumedLogsResource(Resource):
    @marshal_with(consumed_logs_item_fields)
    def post(self):
        consumed_logs_parser = get_consumed_logs_parser()
        args = consumed_logs_parser.parse_args()
        consumed_logs = save_consumed_logs(
            user_id=args["user_id"],
            order_id=args["order_id"],
            quantity=args["quantity"],
        )
        return consumed_logs, HttpStatus.CREATED.value
