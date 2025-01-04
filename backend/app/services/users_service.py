from app.models import Users

def get_all_users(page, per_page):
  users=Users.query.paginate(page = page, per_page = per_page, error_out = False)
  return users
  # return {
  #   'total': users.total,
  #   'pages': users.pages,
  #   'current_page': users.page,
  #   'per_page': users.per_page,
  #   'data': [user.to_dict() for user in users.items]
  # }