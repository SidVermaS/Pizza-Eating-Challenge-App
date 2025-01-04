from app.services.users_service import get_all_users, save_user
from app.serializers.users import user_paginated_fields,user_fields
from app.parsers.common import pagination_parser
from app.parsers.users import get_user_args
from app.models.user.users import Users
from app.consts.api import HttpStatus
from flask_restful import abort, Resource,  marshal_with
from werkzeug.exceptions import BadRequest
class UsersResource(Resource):  
  @marshal_with(user_paginated_fields)
  def get(self):  
    args = pagination_parser.parse_args()    
    users = get_all_users(page = args['page'], per_page = args['per_page'])    
    return users  
  
  @marshal_with(user_fields)
  def post(self):
    try:
      user_parser = get_user_args(required=True)
      args=user_parser.parse_args()
      user = save_user(args)
      return user, HttpStatus.CREATED.value
    except BadRequest as e:
      raise e
      # abort(HttpStatus.UNPROCESSABLE_ENTITY.value, message=e.description)