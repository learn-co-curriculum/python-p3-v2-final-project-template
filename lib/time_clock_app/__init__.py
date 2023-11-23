import sqlite3

CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()

import click

@click.group()
def cli():
    """Time Clocking Application"""
    pass

@click.command()
def clock_in():
    """Clock in for work"""
    # Implementation here
    pass

@click.command()
def clock_out():
    """Clock out of work"""
    # Implementation here
    pass

cli.add_command(clock_in)
cli.add_command(clock_out)

if __name__ == "__main__":
    cli()
