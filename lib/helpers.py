# lib/helpers.py

import typer
from typing import Optional

app = typer.Typer()

@app.command()
def helper_1(name):
# def helper_1(name: str): testing type suggestions
    print("Performing useful function#1.")

@app.command()
def exit_program():
    print("Goodbye!")
    exit()

