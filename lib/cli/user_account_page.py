import click
from cli.pages import define_page, navigate
from classes.User import User
from rich import print
from rich.prompt import Prompt

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
            print('\n[red]Please enter a valid option[/red]\n')

def edit_user(chosen_user):
    global exit

    while not exit:
        choice = click.prompt(f'\nEnter a new name for {chosen_user.name}')
        if not (len(choice) <= 12 and len(choice) >= 1) :
            print('\n[red]Please enter a valid input between 1 and 12[/red]\n')
        else:
            chosen_user.name = choice
            chosen_user.update()

            user_account_page.clear_options()
            new_users = User.get_all()

            for user in new_users:
                user_account_page.add_option(f'{user.name}', lambda user_id = user.id: view_user(user_id))

            print(f'\n[green]Update Successful[/green]\n')

            click.pause()
            exit = True

def delete_user(chosen_user):
    global exit

    while not exit:
        choice = click.prompt(f'\nDelete {chosen_user.name}? (y/n)')
        if choice == 'y':
            confirmation = Prompt.ask(f'\n[red]Are you sure?[/red] (y/n)')
            if confirmation == 'y':
                chosen_user.delete()

                user_account_page.clear_options()
                new_users = User.get_all()

                for user in new_users:
                    user_account_page.add_option(f'{user.name}', lambda user_id = user.id: view_user(user_id))

                print(f'\n[green]{chosen_user.name} was successfully deleted[/green]\n')
                click.pause()
                exit = True
            elif confirmation == 'n':
                print(f'\n[green]Aborting delete of {chosen_user.name}[/green]\n')
                exit = True
            else:
                print('\n[red]Please enter a valid input[/red]\n')
        elif choice == 'n':
            break
        else:
            print('\n[red]Please enter a valid input[/red]\n')
            



user_account_page = define_page("user_account", "Manage User Accounts")

# Add options for user account page

users = User.get_all()

for user in users:
    user_account_page.add_option(f'{user.name}', lambda user_id = user.id: view_user(user_id))


