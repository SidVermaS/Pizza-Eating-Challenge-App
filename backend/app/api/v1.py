from flask import Blueprint
from flask_restful import Api

from app.resources.users import UsersResource

v1_bp = Blueprint('v1',__name__)
api_v1 = Api(v1_bp)

api_v1.add_resource(UsersResource, '/users')