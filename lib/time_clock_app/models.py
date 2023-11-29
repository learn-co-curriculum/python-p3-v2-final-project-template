# models.py
from base import Base 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    time_logs = relationship("TimeLog", back_populates="user")


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
        
    def total_hours_worked(self):
        total_duration = 0
        for log in self.time_logs:
            if log.clock_in_time and log.clock_out_time:
                duration = log.clock_out_time - log.clock_in_time
                total_duration += duration.total_seconds()

        total_hours = total_duration / 3600
        return total_hours