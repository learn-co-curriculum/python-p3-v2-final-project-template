from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Hash this in real applications

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def create(cls, username, password, session):
        """
        Create and add a new user to the database.
        """
        new_user = cls(username=username, password=password)
        try:
            session.add(new_user)
            session.commit()
            print(f"User {username} registered successfully.")
            return new_user
        except SQLAlchemyError as e:
            print(f"Error registering user: {e}")
            session.rollback()
            return None

    @classmethod
    def find_by_username(cls, username, session):
        """
        Find a user by their username.
        """
        try:
            return session.query(cls).filter_by(username=username).first()
        except SQLAlchemyError as e:
            print(f"Error finding user: {e}")
            return None

    # Additional ORM methods like delete, find by id, etc., can be added here

# Database initialization and session creation
engine = create_engine('sqlite:///timeclock.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
new_user = User.create('john_doe', 'secure_password123', session)
found_user = User.find_by_username('john_doe', session)
