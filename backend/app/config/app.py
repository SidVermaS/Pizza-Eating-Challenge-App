from .env import envVariables
class AppConfig:
  SQLALCHEMY_DATABASE_URI= envVariables.DATABASE_URL
  DEBUG = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False