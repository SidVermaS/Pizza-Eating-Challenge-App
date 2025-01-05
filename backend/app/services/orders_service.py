from app.models import Orders, Products,Users
from app.config import db
from app.consts.api import HttpStatus
from flask import jsonify
from werkzeug.exceptions import NotFound
from flask_restful import abort
def save_order(args):
  try:
    product = Products.query.get(args['product_id'])
    user = Users.query.get(args['user_id'])
    
    if product is None:
      raise NotFound(description="Product not found")
    elif user is None:
      raise NotFound(description="User not found")
    
    cost = product.rate * args['quantity']
    
    if(user.coins<cost):
      abort(HttpStatus.UNPROCESSABLE_ENTITY.value, message = "Not enough coins to buy")
      
    user.coins=user.coins-cost    
    new_order = Orders(user_id = args['user_id'], product_id = args['product_id'], quantity = args['quantity'], consumed_count = args['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return new_order
  except Exception as e:
    db.session.rollback()
    raise e

def get_orders(user_id, page, per_page):
  orders = Orders.query.filter_by(user_id = user_id).join(Products, Orders.product_id==Products.id).paginate(page=page, per_page=per_page)
  return {
    'total': orders.total,
    'pages': orders.pages,
    'current_page': orders.page,
    'per_page': orders.per_page,
    'data': orders.items    
  }
    