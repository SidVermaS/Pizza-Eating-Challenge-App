from flask_restful import reqparse
def get_order_parser():
  order_parser=reqparse.RequestParser()
  order_parser.add_argument('user_id', type=str, required=True, location='json', help = 'user_id can\'t be blank')
  order_parser.add_argument('product_id', type=str, required=True, location='json', help = 'product_id can\'t be blank')
  order_parser.add_argument('quantity', type=int, required=True, location='json',)
  return order_parser
