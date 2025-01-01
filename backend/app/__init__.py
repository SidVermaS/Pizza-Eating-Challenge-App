from flask import Flask
from  config import AppConfig, init_db

def create_app():
  app = Flask(__name__)
  
  # Load configuration
  app.config.from_import(AppConfig)
  
  # Initialize database
  init_db(app)
  
  return app