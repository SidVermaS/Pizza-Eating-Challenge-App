from app.resources.v1 import initialize_routes
from flask import Blueprint
from flask_restful import Api

v1_bp = Blueprint("v1", __name__)
api_v1 = Api(v1_bp)

initialize_routes(api_v1)
