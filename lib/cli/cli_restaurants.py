import click

@click.group()
def restaurants():
    """View Restaurants menu."""
    pass

@restaurants.command()
def list_restaurants():
    """List all restaurants."""
    pass

@restaurants.command()
def search_restaurants():
    """Search for a restaurant."""
    pass
