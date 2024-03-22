import click

@click.group()
def visits():
    """View Visits menu."""
    pass

@visits.command()
def list_visits():
    """List all visits."""
    pass

@visits.command()
def add_visit():
    """Add a new visit."""
    pass