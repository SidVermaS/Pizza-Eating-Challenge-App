from flask_restful import fields

product_fields = {
'id': fields.String,
'title': fields.String,
'imagePath': fields.String,
'rate': fields.Integer,
}
product_for_order_fields = {
  'id': fields.String,
  'title': fields.String,
  'imagePath': fields.String,
}
product_paginated_fields={  
  'total':fields.Integer,
  'pages':fields.Integer,
  'current_page':fields.Integer,
  'per_page':fields.Integer,
  'data': fields.List(fields.Nested(product_fields))
}
