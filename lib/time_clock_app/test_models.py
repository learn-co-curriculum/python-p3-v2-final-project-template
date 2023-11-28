import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, User, TimeLog

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def test_create_user(session):
    user = User.create("test_user", "password123", session)
    assert user.username == "test_user"

def test_create_time_log(session):
    user = User.create("test_user", "password123", session)
    log = TimeLog.create(user, session)
    assert log is not None
