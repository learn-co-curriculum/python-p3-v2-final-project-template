# lib/helpers.py
from rich.console import Console
from rich.console import Theme
from rich.table import Table

custom_theme = Theme({
    "heading": "bold bright_white",
    "subhead": "bold gold3",
    "tile": "bold gold3 on blue1"
})

console = Console(theme=custom_theme)

def welcome():
    console.print("""
         _____ _          _____                ___ 
        |_   _| |_ ___   |__   |___ ___    ___|  _|
          | | |   | -_|  |   __| -_|   |  | . |  _|
          |_| |_|_|___|  |_____|___|_|_|  |___|_|  
              _ ______ ____  _____        _____  ______ _    _  _
             | |  ____/ __ \|  __ \ /\   |  __ \|  __  | |  | || |
             | | |__ | |  | | |__) /  \  | |__) | |  | | |__| || |
         _   | |  __|| |  | |  ___/ /\ \ |  _  /| |  | |\___  ||_|
        | |__| | |___| |__| | |  / ____ \| | \ \| |__| |  __| | _
         \____/|______\____/|_| /_/    \_\_|  \_\_____/  |___/ |_|
    """, style="heading")

def menu():
    console.print("Please select an option:", style="subhead")
    print("0. Exit the program")
    print("1. Play a game")
    print("2. View scoreboard")
    print("3. View rules")

def exit_program():
    print("Goodbye!")
    exit()

def find_or_create_player():
    name = input("Enter your name: ").strip()
    player = User.find_by_name(name)

    if player is None:
        new_player = User.create(name)
        print(f"Welcome, {new_player.name}!")
        select_game(new_player)
    else:
        print(f"Welcome back, {player.name}!")
        select_game(player)

table = Table(title="Play the Zen of Jeopardy!")
categories = ["JavaScript", "React", "Python", "SQL", "Computer Science", "Git"]
for category in categories:
    table.add_column(category, style="heading")

table.add_row("$200", "$200", "$200", "$200", "$200", "$200", style="tile")
table.add_row("$400", "$400", "$400", "$400", "$400", "$400", style="tile")
table.add_row("$600", "$600", "$600", "$600", "$600", "$600", style="tile")
table.add_row("$800", "$800", "$800", "$800", "$800", "$800", style="tile")
table.add_row("$1000", "$1000", "$1000", "$1000", "$1000", "$1000", style="tile")

def select_game(current_player):
    console.print(table)

from models.User import User
