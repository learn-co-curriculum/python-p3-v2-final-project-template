# lib/helpers.py

import typer
from typing import Optional

app = typer.Typer()

# @app.command()
# def helper_1(name: str):
#     print("Performing useful function#1.")

@app.command()
def exit_program():
    print("Goodbye!")
    exit()

def list_bands():
    bands = Band.get_all()
    for band in bands:
        print(band)

def find_band_by_name():
    name = input("Enter the band's name: ")
    band = Band.find_by_name(name)
    print(band) if band else print( f'band {name} is not found')

def find_band_by_id():
    id_ = input("Enter the band's id: ")
    band = Band.find_by_id(id_)
    print(band) if band else print(f'Band {id_} is not found')

def create_band():
    name = input("Enter the band's name: ")
    members = input("Enter the band's members: ")
    genre = input("Enter the band's genre: ")
    home_city = input("Enter the band's home city: ")
    try:
        band = Band.create(name, members, genre, home_city)
        print(f'Awesome!: {band} has been created')
    except Exception as exc:
        print("Error creating band: ", exc)

def update_band():
    id_ = input("Enter the band's id: ")
    if band := Band.find_by_id(id_):
        try: 
            name = input("Enter the band's new name: ")
            band.name = name
            members = input("Enter the band's new member(s): ")
            band.members = members
            genre = input("Enter the band's new genre: ")
            band.genre = genre
            band.home_city = input("Enter the band's new home city: ")
            band.home_city = home_city

            band.update()
            print(f'Success in updating: {band}')
        except Exception as exc:
            print("Error updating band: ", exc)
        else:
            print(f'Band {id_} not found')

def delete_band():
    id_ = input("Enter the band's id: ")
    if band := Band.find_by_id(id_):
        band.delete()
        print(f'Band {id_} deleted')
    else:
        print(f'Band {id_} not found')



def list_concerts():
    concerts = Concert.get_all()
    for concert in concerts:
        print(concert)


def find_concert_by_name():
    name = input("Enter the concert's name: ")
    concert = Concert.find_by_name(name)
    print(concert) if concert else print(
        f'Concert {name} not found')


def find_concert_by_id():
    id_ = input("Enter the concert's id: ")
    concert = Concert.find_by_id(id_)
    print(concert) if concert else print(f'Concert {id_} not found')


def create_concert():
    name = input("Enter the concert's name: ")
    date = input("Enter the concert's date: ")
    bands = input("Enter the concert's bands: ")
    city = input("Enter the concert's city: ")
    ticket_cost =("Enter the concert's ticket_cost: ")
    try:
        concert = Concert.create(name,date, bands, city, ticket_cost)
        print(f'Success! {concert} has been created!')
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
            bands = input("Enter the concert's new bands: ")
            concert.bands = bands
            city = input("Enter the concert's new city: ")
            concert.city = city
            concert.ticket_cost = input("Enter the concert's new ticket cost: ")
            concert.ticket_cost = ticket_cost

            concert.update()
            print(f'Success: {concert}')
        except Exception as exc:
            print("Error updating concert: ", exc)
        else:
            print(f'Concert {id_} not found')

def delete_concert():
    id_ = input("Enter the concert's id: ")
    if concert := Concert.find_by_id(id_):
        concert.delete()
        print(f'Concert {id_} deleted')
    else:
        print(f'Concert {id_} not found')




    
    
    
    # export app