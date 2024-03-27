import click
from rich import print
from rich.prompt import Prompt
from cli.pages import navigate
from classes.User import User
from classes.Visit import Visit
from classes.Restaurant import Restaurant

def view_visit(visit_id):
    exit = False
    visit = Visit.get_visit_by_id(visit_id)
    restaurant_obj = Restaurant.get_by_id(visit.restaurant_id)

    print('\n')
    print('[white]=[/white]' * 20)
    print(f'\nDate: {visit.date}')
    print(f'\nRestaurant: [purple]{restaurant_obj.name}[/purple] in [blue]{restaurant_obj.ward}[/blue]')
    print(f'\nDescription: [yellow]{visit.description}[/yellow]')
    print(f'\nRating: [red]{visit.rating}/10[/red]\n')
    print('[white]=[/white]' * 20)
    print('\n')

    while not exit:

        choice = click.prompt(f'Edit or Delete visit? (d/e/x)')
        if choice == 'd':
            confirmation = click.prompt('\nAre you sure you want to delete this visit? (y/n)')
            if confirmation == 'y':
                visit.delete()
                print('\n[red]Visit has been deleted[/red]\n')
                click.pause()
                display_my_visits()
                exit = True
            elif confirmation == 'n':
                print('\n[red]Aborting Delete...[/red]\n')
                click.pause()
                exit = True
            else:
                print('\n[red]Please use a valid input[/red]\n')
        elif choice == 'e':

            edit_choice = click.prompt('\nWhat would you like to change? (1. Rating, 2. Date, 3. Description)')

            if edit_choice == '1':
                rating = Prompt.ask(f'\nChange rating from [#FF7EF5]{visit.rating}[/#FF7EF5] to')
                visit.rating = int(rating)
                visit.update()
                print('\n[green]Updated Rating[green]\n')
                click.pause()
                display_my_visits()
                exit = True
            elif edit_choice == '2':
                date = Prompt.ask(f'\nChange rating from [#FF7EF5]{visit.date}[/#FF7EF5] to')
                visit.date = date
                visit.update()
                print('\n[green]Updated Date[green]\n')
                click.pause()
                display_my_visits()
                exit = True
            elif edit_choice == '3':
                description = Prompt.ask(f'\nChange rating from "[#FF7EF5]{visit.description[0:20]}[/#FF7EF5]" to')
                visit.description = description
                visit.update()
                print('\n[green]Updated Description[green]\n')
                click.pause()
                display_my_visits()
                exit = True
            else:
                print('\n[red]Please use a valid input[/red]\n')
        elif choice == 'x':
            exit = True
        else:
            print('\n[red]Please use a valid input[red]\n')






def display_my_visits():
    from cli.visits_page import visits_page

    exit = False

    user = User.current_user.visits()
    

    if user == []:
        print('\n[red]No Visits Uploaded ... Please upload a visit in the Restaurants Menu[red]\n')
        click.pause()
        navigate('visits')
    else:
        visits_page.options = []

        for visit in user:
            restaurant_obj = Restaurant.get_by_id(visit.restaurant_id)
            visits_page.add_option(f'[yellow]{visit.date}[/yellow] Rating: {visit.rating} <"{visit.description[0:20]}..."> [#FF7EF5]{restaurant_obj.name}[/#FF7EF5] in [blue]{restaurant_obj.ward}[/blue]', lambda visit_id = visit._id: view_visit(visit_id))
            # print(f'\n{visit.date} Rating: {visit.rating} <"{visit.description[0:20]}..."> [#FF7EF5]{restaurant_obj.name}[/#FF7EF5] in [blue]{restaurant_obj.ward}[/blue]')

    return user
        

    

