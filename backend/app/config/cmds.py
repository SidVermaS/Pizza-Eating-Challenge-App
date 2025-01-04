from app.seed.seed import run_seed


def intialize_cmds(app, db):
  @app.cli.command("drop_all")
  def drop_all():
    with app.app_context():
      print("Dropping all tables")
      db.drop_all()
      # with db.engine.connect() as connection:
      #   connection.execute("DROP TABLE IF EXISTS alembic_version")
    
  @app.cli.command("seed")
  def seed():
    run_seed()