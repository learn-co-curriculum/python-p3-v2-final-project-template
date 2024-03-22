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
    sungjin = User.create('Sungjin')
    matteo = User.create('Matteo')


    Visit.create(8, 'I had a great time, the food was sooooo goood!!', '04-30-2023', 1, 46)
    Visit.create(3, 'MEHHH', '04-30-2023', 2, 46)
    Visit.create(4, 'NOT so great', '04-30-2023', 3, 46)
    Visit.create(7, 'Incredible', '04-30-2023', 1, 46)
    Visit.create(5, 'So So', '04-30-2023', 1, 46)
    Visit.create(3, 'I had a great time, the food was sooooo goood!!', '03-13-2024', 2, 46)
    Visit.create(7, 'BEST IN TOWN', '02-30-2022', 1, 46)
    Visit.create(8, 'Great Service', '03-20-2023', 3, 46)
    Visit.create(9, 'Best Restaurant in town', '01-26-2020', 3, 46)





User.drop_table()
Restaurant.drop_table()
Visit.drop_table()

User.create_table()
Restaurant.create_table()
Visit.create_table()

seed_database(tokyo_restaurants)