import click
from cli.pages import define_page, navigate
from classes.User import User
from rich import print

exit = False

def view_user(user_id):
    global exit
    exit = False
    chosen_user = User.get_user_by_id(user_id)

    while not exit:
        choice = click.prompt(f'\nEdit or Delete {chosen_user.name}? (e/d)').lower()
        if choice == 'd':
            delete_user(chosen_user)
        elif choice == 'e':
            edit_user(chosen_user)
            break
        else:
            print('Please enter a valid option')

def edit_user(chosen_user):
    global exit

    while not exit:
        choice = click.prompt(f'\nEnter a new name for {chosen_user.name}')
        if not (len(choice) < 12 and len(choice) > 0) :
            print('Please use a valid input that is between 0 and 12 characters')
        else:
            chosen_user.name = choice
            chosen_user.update()

            user_account_page.clear_options()
            new_users = User.get_all()

            for user in new_users:
                user_account_page.add_option(f'{user.name}', lambda user_id = user.id: view_user(user_id))

            print(f'\nUpdate Successful\n')
            click.pause()
            exit = True

def delete_user(chosen_user):
    global exit

    while not exit:
        choice = click.prompt(f'\nDelete {chosen_user.name}? (y/n)')
        if choice == 'y':
            confirmation = click.prompt(f'\nAre you sure you want to delete {chosen_user.name}? (y/n)')
            if confirmation == 'y':
                chosen_user.delete()

                user_account_page.clear_options()
                new_users = User.get_all()

                for user in new_users:
                    user_account_page.add_option(f'{user.name}', lambda user_id = user.id: view_user(user_id))

                print(f'\n{chosen_user.name} was successfully deleted\n')
                click.pause()
                exit = True
            elif confirmation == 'n':
                print(f'\nAborting delete of {chosen_user.name}')
                exit = True
            else:
                print('Please enter a valid input')
        elif choice == 'n':
            break
        else:
            print('Please use a valid input')
            



user_account_page = define_page("user_account", "Manage User Accounts")

# Add options for user account page

users = User.get_all()

for user in users:
    user_account_page.add_option(f'{user.name}', lambda user_id = user.id: view_user(user_id))


