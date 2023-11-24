from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    time_logs = relationship("TimeLog", back_populates="user")

    # ORM methods like create, delete, etc.

class TimeLog(Base):
    __tablename__ = 'time_logs'

    id = Column(Integer, primary_key=True)
    clock_in_time = Column(DateTime, default=datetime.datetime.now)
    clock_out_time = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="time_logs")

    # ORM methods like create, delete, etc.

# Database initialization
engine = create_engine('sqlite:///timeclock.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example ORM operations
new_user = User(username='john_doe', password='secure_password123')
session.add(new_user)
session.commit()
