from app.resources.v1.users import UserResourceById, UsersResource
from app.resources.v1.products import ProductsResource
from app.resources.v1.orders import OrdersResource, OrdersByUserIdResource
from app.resources.v1.consumed_logs import ConsumedLogsByUserIdResource


def initialize_routes(api):
    api.add_resource(UsersResource, "/users")
    api.add_resource(UserResourceById, "/users/<string:id>")

    api.add_resource(OrdersResource, "/orders")
    api.add_resource(OrdersByUserIdResource, "/orders/users/<string:user_id>")

    api.add_resource(ProductsResource, "/products")

    api.add_resource(
        ConsumedLogsByUserIdResource, "/consumed-logs/users/<string:user_id>"
    )
