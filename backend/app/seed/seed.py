import os
import json

from app.config import db
from app.models import Users #,Products,Orders,ConsumedLogs

# Helper function to read JSON data from a file
def read_json_files(file_name):
  current_dir=os.path.dirname(__file__)
  file_path=os.path.join(current_dir, 'data',file_name)
  with open(file_path, "r") as file:
    return json.load(file)

def seedUsers():
  data=read_json_files('users.data.json')
  # users = [Users(user.id,) for user in data]
  users = [Users(id = user["id"],name = user["name"],age = user["age"],gender = user["gender"],coins = user["coins"],consumed_count = user["consumed_count"], orders=[]) for user in data]
  db.session.add_all(users)

def run_seed(app):   
  with app.app_context(): 
    try:    
      db.session.begin_nested()
      seedUsers()
      db.session.commit()
    except Exception as e:
      print(f"e: {e}")
      db.session.rollback()
    finally:
      db.session.close()
  
  