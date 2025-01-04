from app.services.users_service import get_all_users
from app.serializers.users import user_paginated_fields
from flask_restful import Resource, reqparse, marshal_with

class UsersResource(Resource):  
  @marshal_with(user_paginated_fields)
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('page', type = int, location = 'args', default = 1)
    parser.add_argument('per_page', type = int, location = 'args', default = 10)
    args = parser.parse_args()
    
    result = get_all_users(page = args['page'], per_page = args['per_page'])
    
    return {
    'total': result.total,
    'pages': result.pages,
    'current_page': result.page,
    'per_page': result.per_page,
    'data': result.items
  }
    # return users
    