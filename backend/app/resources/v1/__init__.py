from app.resources.v1.users import UserResourceById, UsersResource

def initialize_routes(api):
  api.add_resource(UsersResource, "/users")
  api.add_resource(UserResourceById, "/users/<string:id>")