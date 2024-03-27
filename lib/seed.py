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
    paul_a = User.create('Paul A')


    Visit.create(8, 'Loved this place!!', '04-30-2023', 1, 1)
    Visit.create(3, 'MEHHH', '04-30-2023', 1, 2)
    Visit.create(2, 'NOT so great', '04-30-2023', 1, 3)
    Visit.create(7, 'Incredible', '04-30-2023', 2, 1)
    Visit.create(5, 'So So', '04-30-2023', 2, 2)
    Visit.create(10, 'Best Ive had!', '03-13-2024', 2, 3)
    Visit.create(7, 'BEST IN TOWN', '02-28-2022', 3, 1)
    Visit.create(8, 'Great Service', '03-20-2023', 3, 2)
    Visit.create(9, 'Best Restaurant in town', '01-26-2020', 3, 3)
    Visit.create(8, 'Shai Halut would approve', '02-28-2022', 4, 1)
    Visit.create(3, 'Bad service is the rating killer', '03-20-2023', 4, 2)
    Visit.create(2, 'Voice from the deep says ITS AIGHT', '01-26-2020', 4, 3)

    Visit.create(8, 'Loved this place!!', '04-30-2023', 1, 4)
    Visit.create(3, 'MEHHH', '04-30-2023', 1, 5)
    Visit.create(2, 'NOT so great', '04-30-2023', 1, 6)
    Visit.create(7, 'Incredible', '04-30-2023', 2, 4)
    Visit.create(5, 'So So', '04-30-2023', 2, 5)
    Visit.create(10, 'Best Ive had!', '03-13-2024', 2, 6)
    Visit.create(7, 'BEST IN TOWN', '02-28-2022', 3, 4)
    Visit.create(8, 'Great Service', '03-20-2023', 3, 5)
    Visit.create(9, 'Best Restaurant in town', '01-26-2020', 3, 6)
    Visit.create(8, 'Shai Halut would approve', '02-28-2022', 4, 4)
    Visit.create(3, 'Bad service is the rating killer', '03-20-2023', 4, 5)
    Visit.create(5, 'Voice from the deep says ITS AIGHT', '01-26-2020', 4, 6)




User.drop_table()
Restaurant.drop_table()
Visit.drop_table()

User.create_table()
Restaurant.create_table()
Visit.create_table()

seed_database(tokyo_restaurants)





# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

print(Restaurant.get_by_id(1).visits())






