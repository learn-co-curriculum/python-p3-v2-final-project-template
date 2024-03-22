import csv
from classes.Restaurant import Restaurant
from classes.Visit import Visit
from classes.User import User

tokyo_restaurants = 'lib/data/tokyo_restaurants.csv'

def seed_database(csv_file):
    # Read data from CSV file
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file)
        data = [Restaurant.instance_from_db(row) for row in reader]

        for instance in data:
            instance.save()

    christian = User.create('Christian')
    print(christian)
    User.create('Sungjin')

    Visit.create(2, 'Description', 'Date', 'USER', 'Restaurant')

User.drop_table()
Restaurant.drop_table()
Visit.drop_table()

User.create_table()
Restaurant.create_table()
Visit.create_table()

seed_database(tokyo_restaurants)