from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
import datetime

engine = create_engine('sqlite:///timeclock.db')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Password should be hashed in real application
    time_logs = relationship("TimeLog", back_populates="user")

    # ORM Methods for User
    @classmethod
    def create(cls, username, password, session):
        new_user = cls(username=username, password=password)
        try:
            session.add(new_user)
            session.commit()
            return new_user
        except SQLAlchemyError as e:
            print(f"Error creating user: {e}")
            session.rollback()
            return None

    # Additional ORM methods like delete, find by id, etc., can be added here

class TimeLog(Base):
    __tablename__ = 'time_logs'

    id = Column(Integer, primary_key=True)
    clock_in_time = Column(DateTime, default=datetime.datetime.now)
    clock_out_time = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="time_logs")

    # ORM Methods for TimeLog
    @classmethod
    def create(cls, user, session):
        new_log = cls(user=user)
        try:
            session.add(new_log)
            session.commit()
            return new_log
        except SQLAlchemyError as e:
            print(f"Error creating time log: {e}")
            session.rollback()
            return None

    # Additional ORM methods like delete, find by id, etc., can be added here

def initialize_db():
    engine = create_engine('sqlite:///timeclock.db')
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    initialize_db()
