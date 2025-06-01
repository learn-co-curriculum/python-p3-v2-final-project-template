# main.py

from lib.database import Base, engine
from lib.models.models import Book

def setup_database():
    Base.metadata.create_all(engine)
    print("Database and tables created!")

if __name__ == "__main__":
    setup_database()
