import datetime
from sqlalchemy import create_engine, Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
from database import User  # Ensure this import matches your project structure

Base = declarative_base()

class TimeLog(Base):
    __tablename__ = 'time_logs'

    id = Column(Integer, primary_key=True)
    clock_in_time = Column(DateTime, default=datetime.datetime.now)
    clock_out_time = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="time_logs")

    def __init__(self, user):
        self.user = user

    @classmethod
    def clock_in(cls, user, session):
        """ Record the clock-in time for the user """
        new_log = cls(user=user)
        try:
            session.add(new_log)
            session.commit()
            print(f"Clocked in at {new_log.clock_in_time}")
            return new_log
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            session.rollback()
            return None

    @classmethod
    def clock_out(cls, user, session):
        """ Record the clock-out time for the user """
        try:
            # Find the latest time log without a clock_out_time
            log = session.query(cls).filter_by(user=user, clock_out_time=None).first()
            if log:
                log.clock_out_time = datetime.datetime.now()
                session.commit()
                print(f"Clocked out at {log.clock_out_time}")
            else:
                print("No active time log found.")
        except SQLAlchemyError as e:
            print(f"Database error: {e}")
            session.rollback()

# Initialize database connection and session
engine = create_engine('sqlite:///timeclock.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
# Assuming 'user' is an instance of the User class
# time_log = TimeLog.clock_in(user, session)
# time_log = TimeLog.clock_out(user, session)
