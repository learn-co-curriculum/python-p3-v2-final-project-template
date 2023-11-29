import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.exc import SQLAlchemyError
from base import Base
from models import User

class TimeLog(Base):
    __tablename__ = 'time_logs'
    __table_args__ = {'extend_existing': True}

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


