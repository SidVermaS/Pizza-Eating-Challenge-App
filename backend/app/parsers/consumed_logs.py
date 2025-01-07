from flask_restful import reqparse


def get_consumed_logs_parser():
    order_parser = reqparse.RequestParser()
    order_parser.add_argument(
        "user_id",
        type=str,
        required=True,
        location="json",
        help="user_id can't be blank",
    )
    order_parser.add_argument(
        "order_id",
        type=str,
        required=True,
        location="json",
        help="order_id can't be blank",
    )
    order_parser.add_argument(
        "consumed_count",
        type=int,
        required=True,
        location="json",
    )
    return order_parser
