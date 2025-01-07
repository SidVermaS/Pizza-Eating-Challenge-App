from app.services.users_service import get_users, save_user, update_user, delete_user
from app.serializers.users import user_paginated_fields, user_fields
from app.parsers.users import get_user_parser, get_users_parser
from app.consts.api import HttpStatus

from flask_restful import Resource, marshal_with
from werkzeug.exceptions import BadRequest


class UsersResource(Resource):
    @marshal_with(user_paginated_fields)
    def get(self):

        users_parser = get_users_parser()
        args = users_parser.parse_args()
        users = get_users(page=args["page"], per_page=args["per_page"], sort_by=args['sort_by'])
        return users, HttpStatus.OK.value

    @marshal_with(user_fields)
    def post(self):
        try:
            user_parser = get_user_parser(required=True)
            args = user_parser.parse_args()
            user = save_user(args)
            return user, HttpStatus.CREATED.value
        except BadRequest as e:
            raise e
            # abort(HttpStatus.UNPROCESSABLE_ENTITY.value, message=e.description)


class UserResourceById(Resource):
    @marshal_with(user_fields)
    def patch(self, id):
        try:
            user_parser = get_user_parser(required=False)
            args = user_parser.parse_args()
            user = update_user(id, args)
            return user, HttpStatus.OK.value
        except BadRequest as e:
            raise e

    def delete(self, id):
        try:
            delete_user(id)
            return None, HttpStatus.NO_CONTENT.value
        except BadRequest as e:
            raise e
