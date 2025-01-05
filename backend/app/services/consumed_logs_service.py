from app.models.challenge.consumedLogs import ConsumedLogs
from app.models.product.products import Products
from app.models.order.orders import Orders


def get_consumed_logs(user_id, page, per_page):
  consumed_logs = ConsumedLogs.query.filter_by(user_id=user_id).join(Products, ConsumedLogs.product_id==Products.id).paginate(page=page,per_page=per_page)
  return {
    'total': consumed_logs.total,
    'pages': consumed_logs.pages,
    'current_page': consumed_logs.page,
    'per_page': consumed_logs.per_page,
    'data': consumed_logs.items    
  }