from app.serializers.products import product_paginated_fields
from app.parsers.common import get_pagination_parser
from app.services.products_service import get_all_products
from flask_restful import Resource, marshal_with


class ProductsResource(Resource):
    @marshal_with(product_paginated_fields)
    def get(self):
        pagination_parser = get_pagination_parser()
        args = pagination_parser.parse_args()
        products = get_all_products(page=args["page"], per_page=args["per_page"])
        return products
