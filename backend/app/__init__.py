
from flask import Flask

from app.config import DBConfig, db, init_db, setup

def create_app():
  app = Flask(__name__)
  
  # Load configuration
  app.config.from_object(DBConfig)  
  # Initialize database
  init_db(app)  
  return app

app = create_app()

setup(app, db)
if __name__ == "main":
  app.run()