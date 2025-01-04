from app.resources.users import UsersResource

def initialize_routes(api):
  api.add_resource(UsersResource, "/users")