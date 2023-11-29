# base.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Create the base class for declarative class definitions
Base = declarative_base()

# Create an engine that the Session will use for connection resources
engine = create_engine('sqlite:///timeclock.db')
