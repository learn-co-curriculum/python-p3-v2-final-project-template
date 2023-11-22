from models.players import Player

def create_new_player():
    existing_players = [player.name.lower().strip() for player in Player.all()]

    player_info = {
        'name' : '',
        'password' : '',
        'age' : ''
    }   
    creating = True
    while creating:
        while True:
            print("Enter your name:")
            name = input("❯❯ ")
            if name.lower().strip() not in existing_players:
                if len(name) != 0:
                    player_info['name'] = name
                    break
                else:
                    print('Player name must be at least 1 character!')
            else:
                print('Player name already exists!')
        while True:
            print("Enter a password (must be at least 5 characters): ")
            password = input("❯❯ ")
            if len(password) >= 5:
                player_info['password'] = password
                break
            else:
                print('Password must be at least 5 characters')
        while True:
            print("Enter your age:")
            age = input('❯❯ ')
            try:
                age = int(age)
                if age >= 18:
                    player_info['age'] = age
                    break
                else:
                    print('✖ ✖ You must be 18 or over to play. Goodbye! ✖ ✖')
                    return
            except ValueError:
                print("age must be a valid number")
        print('Your profile:')
        print(f'→ Name: {player_info["name"]}')
        print(f'→ Password: {player_info["password"]}')
        print(f'→ Age: {player_info["age"]}')
        print("Confirm your profile (Y/N)?")
        while True:
            choice = input("❯❯ ")    
            if choice == "Y":
                Player.create(
                    player_info['name'],
                    player_info['password'],
                    player_info['age']
                )
                print("✔ ✔ SUCCESS ✔ ✔")
                print("Your player profile has been saved!")
                print("Returning to the main menu...")
                creating = False
                break
            elif choice == "N":
                print("✖ ✖ CANCELLED ✖ ✖")
                print("Returning to Main Menu...")
                creating = False
                break
            else:
                print("Type Y or N to confirm or restart your new Player Profile")