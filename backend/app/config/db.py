from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from env import envVariables
db=SQLAlchemy()
migrate = Migrate()

def init_db(app):
  app.config['SQLALCHEMY_DATABASE_URI']=envVariables.DATABASE_URL
  db.init_app(app)
  migrate.init_app(app, db)