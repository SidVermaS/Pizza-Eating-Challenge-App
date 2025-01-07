from flask_restful import reqparse


def get_pagination_parser():
    pagination_parser = reqparse.RequestParser()
    pagination_parser.add_argument("page", type=int, location="args", default=1)
    pagination_parser.add_argument("per_page", type=int, location="args", default=10)
    return pagination_parser
