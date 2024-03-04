# lib/helpers.py

import typer
from typing import Optional

app = typer.Typer()

@app.command()
def helper_1(name: str):
    print("Performing useful function#1.")

@app.command()
def exit_program():
    print("Goodbye!")
    exit()

# export app