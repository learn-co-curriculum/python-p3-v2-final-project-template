from models.players import Player

def create_new_player():
    existing_players = [player.name.lower().strip() for player in Player.all()]

    player_info = {
        'name' : '',
        'password' : '',
        'age' : '',
        'next_game' : ''
    }   
    creating = True
    while creating:
        while True:
            name = input("Enter your name: ")
            if name.lower().strip() not in existing_players:
                if len(name) != 0:
                    player_info['name'] = name
                    break
                else:
                    print('Player name must be at least 1 character!')
            else:
                print('Player name already exists!')
        while True:
            password = input("Enter a password (must be at least 5 characters): ")
            if len(password) >= 5:
                player_info['password'] = password
                break
            else:
                print('Password must be at least 5 characters')
        while True:
            age = input('Tell us your age: ')
            try:
                age = int(age)
                if age >= 18:
                    player_info['age'] = age
                    break
                else:
                    print('You must be 18 or over to play. Goodbye!')
                    break
            except ValueError:
                print("age must be a valid number.")
        while True: 
            next_game = input('Will you be playing in the next game? (Y/N): ')
            if next_game == 'Y':
                player_info['next_game'] = 1
                break
            elif next_game == 'N': 
                player_info['next_game'] = 0
                break
            else:
                print("Your answer must be Y or N")
        print('Your profile:')
        print(f'→ Name: {player_info["name"]}')
        print(f'→ Password: {player_info["password"]}')
        print(f'→ Age: {player_info["age"]}')
        print(f'→ Will be in next game: {"Yes" if player_info["next_game"] else "No"}')
        print("Confirm your profile (Y/N)?")
        while True:
            choice = input("> ")    
            if choice == "Y":
                Player.create(
                    player_info['name'],
                    player_info['password'],
                    player_info['age'],
                    next_game=player_info['next_game']
                )
                print("✔ ✔ SUCCESS ✔ ✔")
                print("Your player profile has been saved!")
                print("Returning to the main menu...")
                creating = False
                break
            elif choice == "N":
                print("✖ ✖ CANCELLED ✖ ✖")
                print("Restarting Player Creation Form...")
                break
            else:
                print("Type Y or N to confirm or restart your new Player Profile")