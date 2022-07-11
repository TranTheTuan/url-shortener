from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import get_settings

# engine: entry to database
# check_same_thread: False to allow multiple threads to access the same connection
engine = create_engine(get_settings().db_url, connect_args={"check_same_thread": False})

# You’ll create a working database session when you instantiate SessionLocal later
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base returns a class that connects the database engine to the SQLAlchemy functionality of the models
# Base will be the class that the database model inherits
Base = declarative_base()
