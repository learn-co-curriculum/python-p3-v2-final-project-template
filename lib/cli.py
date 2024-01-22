# lib/cli.py

from helpers import (
    exit_program,
    create_new_player,
    list_all_players,
    update_player,
    delete_player,
    list_all_levels,
    new_game
)

from models.player import Player
from models.level import Level
from models.game import Game
from termcolor import colored, cprint
from difflib import Differ, SequenceMatcher
import time

def main():
    while True:
        print("---Python Type-On---")
        print("Welcome to Python Type-On!")
        
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            
            playing = True
            player = None
            level = 1

            while playing == True:
                if player == None:
                    player = create_new_player()
                else:
                    #get the string from level:
                    current_level = Level.find_by_id(level)

                    if current_level == None:
                        print("Congrats, you've reached the end of the game!")
                        exit()

                    print(f"{current_level.name} - {current_level.difficulty}")
                    cprint(current_level.string, "cyan")

                    #start timer
                    start_timer = time.time()

                    # prompt user for input:
                    player_input = input()
                    print(f"You entered: {player_input}")

                    # stop timer
                    stop_timer = time.time()

                    # compute diff between string and input:
                    d = Differ()
                    s = SequenceMatcher(None, current_level.string, player_input)
                    result = list(d.compare(current_level.string, player_input))

                    formatted_result = [colored(letter, "red") if letter[0] == "-" or letter[0] == "+" else colored(letter, "green") for letter in result]

                    # calculate accuracy and speed
                    accuracy = s.quick_ratio() * 100
                    speed = stop_timer - start_timer
                    
                    # instantiate a new game to store data
                    new_game = Game.create(player.id, current_level.id, player_input, speed, accuracy)

                    #print game results (player input, time and accuracy)
                    print(''.join(formatted_result))
                    print(f"Accuracy: {accuracy}%")
                    print(f"Speed: {speed} seconds")

                    if accuracy < 80:
                        try_again = input("Your accuracy was less than 80%. Would you like to try again? ")
                        if try_again == "Y":
                            level
                        elif try_again == "N":
                            exit()
                        else:
                            print("Please answer Y or N")
                    else:
                        keep_playing = input("Would you like to keep playing? ")
                        
                        if keep_playing == "Y":
                            level += 1
                        elif keep_playing == "N":
                            exit()
                        else:
                            print("Please answer Y or N")
                   
        elif choice == "2":
            list_all_players()
        elif choice == "3":
            update_player()
        elif choice == "4":
            delete_player()
        elif choice == "5":
            list_all_levels()
        elif choice == "6":
            pass
        elif choice == "7":
            pass
        elif choice == "8":
            pass
        else:
            print("Invalid choice")


def menu():
    
    print("0. Exit the program")
    print("1. New game")
    print("2. List all players")
    print("3. Update player")
    print("4. Delete player")
    print("5. List all levels")
    print("6. Player avg accuracy and speed")
    print("7. List of players by avg accuracy")
    print("8. List of players by avg speed")

if __name__ == "__main__":
    main()
