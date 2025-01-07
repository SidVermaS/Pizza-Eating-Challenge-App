from app.models import Users
from app.config import db

from werkzeug.exceptions import BadRequest, NotFound


def get_users(page, per_page):
    users = Users.query.paginate(page=page, per_page=per_page, error_out=False)
    return {
        "total": users.total,
        "pages": users.pages,
        "current_page": users.page,
        "per_page": users.per_page,
        "data": users.items,
    }


def save_user(args):
    lowest_ranked_user = Users.query.order_by(Users.rank.desc()).first()
    new_user = Users(
        name=args["name"],
        age=args["age"],
        gender=args["gender"],
        rank=(
            lowest_ranked_user.rank
            if lowest_ranked_user.consumed_count == 0
            else lowest_ranked_user.rank + 1
        ),
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user


def update_user(id, args):
    if not args:
        raise BadRequest(description="Payload is empty")
    user = Users.query.get(id)
    if not user:
        raise NotFound(description="User not found")

    for key, value in args.items():
        if value is not None and hasattr(user, key):
            setattr(user, key, value)
    db.session.commit()
    return user


def delete_user(id):
    user = Users.query.get(id)
    if not user:
        raise NotFound(description="User not found")
    db.session.delete(user)
    db.session.commit()
