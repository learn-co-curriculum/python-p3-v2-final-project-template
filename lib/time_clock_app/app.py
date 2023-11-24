import click
from database import User, TimeLog, initialize_db, sessionmaker, create_engine

# Initialize the database
initialize_db()

# Create a session
engine = create_engine('sqlite:///timeclock.db')
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """Time Clocking Application"""
    pass

@click.command()
def clock_in():
    """Clock in for work"""
    # Example: hard-coded user ID and time log
    user_id = 1  # Replace with the actual user's ID
    new_time_log = TimeLog(user_id=user_id)
    session.add(new_time_log)
    session.commit()
    print("Clocked in.")

@click.command()
def clock_out():
    """Clock out of work"""
    # Example: hard-coded user ID and updating the latest time log
    user_id = 1  # Replace with the actual user's ID
    time_log = session.query(TimeLog).filter_by(user_id=user_id, clock_out_time=None).first()
    if time_log:
        time_log.clock_out_time = datetime.datetime.now()
        session.commit()
        print("Clocked out.")
    else:
        print("No active time log found to clock out.")

cli.add_command(clock_in)
cli.add_command(clock_out)

if __name__ == "__main__":
    cli()
