from models.players import Player

def create_new_player():
    existing_players = [player.name for player in Player.all()]

    player_info = {
        'name' : '',
        'password' : '',
        'age' : '',
        'next_game' : ''
    }   
    creating = True
    while creating:
        while player_info['name'] == '':
            name = input("Enter your name: ")
            if name not in existing_players:
                player_info['name'] = name
            else:
                print('Player name already exists!')
        while player_info['password'] == '':
            password = input("Enter a password (must be at least 5 characters): ")
            if len(password) >= 5:
                player_info['password'] = password
            else:
                print('Password must be at least 5 characters')
        age = input('Tell us your age: ')
        if int(age) >= 18:
            player_info['age'] = int(age)
        else:
            print('You must be 18 or over to play. Goodbye!')
            break
        next_check = True
        while next_check: 
            next_game = input('Will you be playing in the next game? (Y/N): ')
            if next_game == 'Y':
                player_info['next_game'] = 1
                next_check = False
            elif next_game == 'N': 
                player_info['next_game'] = 0
                next_check = False
            else:
                print("Your answer must be Y or N")
        print('Your profile:')
        print(f'→ Name: {player_info["name"]}')
        print(f'→ Password: {player_info["password"]}')
        print(f'→ Age: {player_info["age"]}')
        print(f'→ Will be in next game: {"Yes" if player_info["next_game"] else "No"}')
        print("Confirm your profile (Y/N)?")
        confirming = True
        while confirming:
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
                confirming = False
                creating = False
            elif choice == "N":
                print("✖ ✖ CANCELLED ✖ ✖")
                print("Restarting Player Creation Form...")
                confirming = False
            else:
                print("Type Y or N to confirm or restart your new Player Profile")