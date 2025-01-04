from flask import Flask

from app.config import DBConfig, init_db, db
from app.seed import run_seed

def create_app():
  app = Flask(__name__)
  
  # Load configuration
  app.config.from_object(DBConfig)  
  # Initialize database
  init_db(app)  
  return app

app = create_app()

@app.cli.command("drop_all")
def drop_all():
  with app.app_context():
    print("Dropping all tables")
    db.drop_all()
    with db.engine.connect() as connection:
      connection.execute("DROP TABLE IF EXISTS alembic_version")
    
@app.cli.command("seed")
def seed_all():
  run_seed()
  
if __name__ == "main":
  app.run()