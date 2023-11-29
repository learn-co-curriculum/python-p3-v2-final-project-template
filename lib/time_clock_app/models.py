# models.py
from base import Base  # Import Base from base.py
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
    # Define any additional ORM methods like create, delete, etc., for User
