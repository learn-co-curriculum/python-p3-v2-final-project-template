# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from models import User
from timelog import TimeLog

engine = create_engine('sqlite:///timeclock.db')
Session = sessionmaker(bind=engine)

def initialize_db():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    initialize_db()
