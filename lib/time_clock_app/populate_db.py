from faker import Faker
import random
from sqlalchemy.orm import sessionmaker
from database import User, TimeLog, engine
import datetime

fake = Faker()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def create_fake_users(num_users=10):
    for _ in range(num_users):
        username = fake.user_name()
        password = fake.password()
        user = User.create(username, password, session)
        if user:
            create_fake_time_logs(user, random.randint(5, 20))

def create_fake_time_logs(user, num_logs):
    for _ in range(num_logs):
        clock_in_time = fake.date_time_this_month()
        clock_out_time = clock_in_time + datetime.timedelta(hours=random.randint(1, 8))
        time_log = TimeLog(user=user, clock_in_time=clock_in_time, clock_out_time=clock_out_time)
        session.add(time_log)
    session.commit()

if __name__ == "__main__":
    create_fake_users()
