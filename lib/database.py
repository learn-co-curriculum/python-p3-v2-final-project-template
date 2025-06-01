# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use SQLite for simplicity
engine = create_engine("sqlite:///library.db", echo=False)
Session = sessionmaker(bind=engine)

# Base class for models
Base = declarative_base()
