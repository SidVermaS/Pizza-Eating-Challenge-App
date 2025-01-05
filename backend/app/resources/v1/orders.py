from app.serializers.orders import order_fields
from app.services.orders_service import get_orders, save_order
from app.parsers.orders import get_order_parser
from app.consts.api import HttpStatus
from app.serializers.orders import orders_paginated_fields
from app.parsers.common import get_pagination_parser
from flask_restful import Resource, marshal_with

class OrdersResource(Resource):
  @marshal_with(order_fields)
  def post(self):
    order_parser = get_order_parser() 
    args=order_parser.parse_args()
    order = save_order(args)
    return order, HttpStatus.CREATED.value

class OrdersByUserIdResource(Resource):
  @marshal_with(orders_paginated_fields)
  def get(self,user_id):
    pagination_parser=get_pagination_parser()
    args = pagination_parser.parse_args()
    
    orders =  get_orders(user_id = user_id, page = args['page'], per_page = args['per_page'])  
    return orders, HttpStatus.OK.value