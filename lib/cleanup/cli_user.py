import click

@click.group()
def user_account(ctx):
    """User account commands."""
    pass

@user_account.command('view-profile')
def view_profile():
    """View user profile."""
    pass

@user_account.command('edit-profile')
def edit_profile():
    """Edit user profile."""
    pass

def user_account_menu():
    """Displays the user account menu and prompts for action."""
    click.echo("\nUser Account Menu:")
    click.echo("1: View Profile")
    click.echo("2: Edit Profile")
    click.echo("x: Back to Main Menu")

    user_account_options = {
        '1': view_profile,
        '2': edit_profile,
    }

    while True:
        choice = click.prompt("Please enter your choice", type=str)

        if choice in user_account_options:
            click.clear()
            user_account_options[choice]()  # Invoke the chosen function
        elif choice == 'x':
            click.clear()
            break  #exit the user_account_menu
        else:
            click.echo("Invalid choice. Please try again.")