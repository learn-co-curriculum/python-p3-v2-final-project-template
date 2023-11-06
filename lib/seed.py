from models.User import User

def drop_tables():
    User.drop_table()

def create_tables():
    User.create_table()

if __name__ == "__main__":
    drop_tables()
    print("Tables dropped!")
    create_tables()
    print("Tables created!")
    # seed_tables()
    # print("Seed data complete!")