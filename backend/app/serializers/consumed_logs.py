from flask_restful import fields
from app.serializers.products import product_for_order_fields
consumed_logs_item_fields={
  'id': fields.String,
  'order_id': fields.String,
  'product': fields.Nested(product_for_order_fields),  
  'consumed_count': fields.Integer,
  'created_at': fields.DateTime
}

consumed_logs_paginated_fields={  
'total':fields.Integer,
'pages':fields.Integer,
'current_page':fields.Integer,
'per_page':fields.Integer,
'data': fields.List(fields.Nested(consumed_logs_item_fields))
}