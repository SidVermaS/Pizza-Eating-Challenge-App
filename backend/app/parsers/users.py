from app.types.users import gender_type
from app.consts.user import GenderE
from flask_restful import reqparse

def get_user_parser(required=True):
  user_parser=reqparse.RequestParser()
  user_parser.add_argument('name', type=str, required=required, location='json', help = 'name can\'t be blank')
  user_parser.add_argument('age', type=int, required=required, location='json', help = 'age can\'t be blank')
  user_parser.add_argument('gender', type=gender_type, required=required, location='json', help=f"GenderE should be one of {[gender.value for gender in GenderE ]}")
  user_parser.add_argument('coins', type=int, required=False, location='json',)
  return user_parser