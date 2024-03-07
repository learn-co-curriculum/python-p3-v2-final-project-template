# lib/helpers.py
from models.band import Band
from models.city import City
from models.concert import Concert
from models.seed import reseed

# import typer
# from typing import Optional

# app = typer.Typer()

# in the future, i won't lazily just do type conversions with the inputs
# the classes should be able to vet for strings, or the helpers should at least have their own validation

def exit_program():
    print("Goodbye!")
    exit()

def list_bands():
    Band.show_all()

def find_band_by_name():
    name = input("Enter the band's name: ")
    band = Band.find_by_name(name)
    print(band) if band else print( f'band {name} is not found')

def find_band_by_id():
    id_ = int(input("Enter the band's id: "))
    band = Band.find_by_id(id_)
    print(band) if band else print(f'Band {id_} is not found')

def create_band():
    name = input("Enter the band's name: ")
    members = input("Enter the band's members separated by commas (and spaces): ").split(", ")
    genre = input("Enter the band's genre: ")
    home_city = input("Enter the band's home city: ")
    try:
        band = Band.create(name, members, genre, home_city)
        print(f'Awesome!: The band has been created!\n{band}')
    except Exception as exc:
        print("Error creating band: ", exc)

def update_band():
    id_ = input("Enter the band's id: ")
    if band := Band.find_by_id(id_):
        try: 
            name = input("Enter the band's new name: ")
            band.name = name
            members = input("Enter the band's new member(s) separated by commas (and spaces): ").split(", ")
            band.members = members
            genre = input("Enter the band's new genre: ")
            band.genre = genre
            band.home_city = input("Enter the band's new home city: ")
            band.home_city = home_city

            band.update()
            print(f'Success in updating: \n{band}')
        except Exception as exc:
            print("Error updating band: ", exc)
        else:
            print(f'Band {id_} not found')

def delete_band():
    id_ = int(input("Enter the band's id: "))
    if band := Band.find_by_id(id_):
        band.delete()
        print(f'Band {id_} deleted')
    else:
        print(f'Band {id_} not found')



def list_concerts():
    Concert.show_all()

def find_concert_by_name():
    name = input("Enter the concert's name: ")
    concert = Concert.find_by_name(name)
    print(concert) if concert else print(
        f'Concert {name} not found')


def find_concert_by_id():
    id_ = int(input("Enter the concert's id: "))
    concert = Concert.find_by_id(id_)
    print(concert) if concert else print(f'Concert {id_} not found')


def create_concert():
    name = input("Enter the concert's name: ")
    date = input("Enter the concert's date: ")
    bands = input("Enter the concert's bands separated by commas (and spaces): ").split(", ")
    city = input("Enter the concert's city: ")
    # ticket_cost =("Enter the concert's ticket_cost: ")
    ticket_cost = {"Four-day pass": [400, 1000], "Friday pass": [110, 900]}
    try:
        concert = Concert.create(name, date, bands, city, ticket_cost)
        print(f'Success! The concert has been created! \n{concert}')
    except Exception as exc:
        print("Error creating concert: ", exc)


def update_concert():
    id_ = input("Enter the concert's id: ")
    if concert := Concert.find_by_id(id_):
        try:
            name = input("Enter the concert's new name: ")
            concert.name = name
            concert = input("Enter the concert's new date: ")
            concert.date = date
            bands = input("Enter the concert's new bands separated by commas (and spaces): ")
            concert.bands = bands
            city = input("Enter the concert's new city: ")
            concert.city = city
            # concert.ticket_cost = input("Enter the concert's new ticket cost: ")
            # concert.ticket_cost = ticket_cost
            concert.ticket_cost = {"Four-day pass": [400, 1000], "Friday pass": [110, 900]}

            concert.update()
            print(f'Success: {concert}')
        except Exception as exc:
            print("Error updating concert: ", exc)
        else:
            print(f'Concert {id_} not found')

def delete_concert():
    id_ = int(input("Enter the concert's id: "))
    if concert := Concert.find_by_id(id_):
        concert.delete()
        print(f'Concert {id_} deleted')
    else:
        print(f'Concert {id_} not found')

def seed():
    reseed()