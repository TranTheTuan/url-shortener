import secrets
import string
from sqlalchemy.orm import Session
from . import crud

def create_random_key(length=5):
  chars = string.ascii_uppercase + string.digits
  return "".join(secrets.choice(chars) for _ in range(length))

def create_unique_random_key(db: Session):
  key = create_random_key()
  while crud.get_db_url_by_key(db, key):
    key = create_random_key()
  return key