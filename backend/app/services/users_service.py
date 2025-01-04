from app.models import Users
from app.config import db

def get_all_users(page, per_page):
  users=Users.query.paginate(page = page, per_page = per_page, error_out = False)
  return {
    'total': users.total,
    'pages': users.pages,
    'current_page': users.page,
    'per_page': users.per_page,
    'data': users.items
  }
def save_user(args):
  new_user = Users(name = args['name'],age = args['age'],gender = args['gender'])
  db.session.add(new_user)
  db.session.commit()
  return new_user