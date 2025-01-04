from .env import envVariables
class DBConfig:
  SQLALCHEMY_DATABASE_URI=envVariables.DATABASE_URL
  DEBUG = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False