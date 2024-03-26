import click

class Page:
    def __init__(self, title):
        self.title = title
        self.options = []

    def add_option(self, text, action):
        self.options.append((text, action))
    
    def clear_options(self):
        self.options = []

pages = {}
current_page = None
previous_pages = []

def define_page(id, title):
    new_page = Page(title)
    pages[id] = new_page
    return new_page

def navigate(page_id):
    global current_page
    previous_pages.append(current_page)
    current_page = pages[page_id]

def go_back():
    global current_page

    if previous_pages:
        current_page = previous_pages.pop()
    else:
        print('\nYou are in the home page\n')


def draw_page():
    click.clear()
    click.echo(current_page.title)
    click.echo("=" * len(current_page.title))
    click.echo()

    for index, option in enumerate(current_page.options, start=1):
        click.echo(f"{index}. {option[0]}")
    click.echo()

    click.echo("x. Return to the previous page")
    click.echo("q. Exit the program")

def handle_user_input(input):
    if input == 'q':
        exit_program()
    elif input == 'x':
        if not len(previous_pages) == 1:
            go_back()
        else:
            print('\nNo previous page found')

    elif input.isdigit():
        index = int(input)
        if 1 <= index <= len(current_page.options):
            action = current_page.options[index - 1][1]
            action()
        else:
            click.echo("Invalid input. Please try again.")
    else:
        click.echo("Invalid input. Please try again.")

def exit_program():
    click.echo("Exiting the program...")
    exit()