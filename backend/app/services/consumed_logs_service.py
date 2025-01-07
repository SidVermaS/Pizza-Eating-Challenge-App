from app.config import db
from app.models.consumed_logs import ConsumedLogs
from app.models.products import Products
from app.models.orders import Orders
from app.models.users import Users
from app.services.users_service import update_rank
from werkzeug.exceptions import NotFound, UnprocessableEntity


def get_consumed_logs(user_id, page, per_page):
    consumed_logs = (
        ConsumedLogs.query.filter_by(user_id=user_id)
        .join(Products, ConsumedLogs.product_id == Products.id)
        .paginate(page=page, per_page=per_page)
    )
    return {
        "total": consumed_logs.total,
        "pages": consumed_logs.pages,
        "current_page": consumed_logs.page,
        "per_page": consumed_logs.per_page,
        "data": consumed_logs.items,
    }


def save_consumed_logs(user_id, order_id, quantity):
    order = Orders.query.filter_by(id=order_id, user_id=user_id)
    if order is None:
        raise NotFound(description="Order not found")
    elif order.user_id != user_id:
        raise UnprocessableEntity(description="order is unavailable for this user")
    elif order.quantity < quantity:
        raise UnprocessableEntity(
            description="quantity to be logged is greater than the available quantity"
        )
    user = Users.query.get(user_id)
    try:
        user.consumed_count += quantity
        order.consumed_count += quantity
        order.quantity -= quantity
        new_consumed_log = ConsumedLogs(
            consumed_count=quantity, user_id=user_id, product_id=order.product_id
        )
        db.session.add(new_consumed_log)
        db.session.commit()
    except:
        db.session.rollback()
        return None
    update_rank()