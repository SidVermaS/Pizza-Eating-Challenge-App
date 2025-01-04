
from flask import Flask

from app.config import DBConfig, db, init_db, setup
from app.api.v1 import v1_bp
def create_app():
  app = Flask(__name__)
  
  # Load configuration
  app.config.from_object(DBConfig)  
  # Initialize database
  init_db(app)  
  
  app.register_blueprint(v1_bp, url_prefix='/api/v1')
  
  return app

app = create_app()

setup(app, db)
if __name__ == "main":
  app.run()