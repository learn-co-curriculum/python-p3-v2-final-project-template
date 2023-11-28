# lib/helpers.py
from time_clock_app.user_info import Username


def create_username():
    user = input("enter unsername: ")
    username = Username(user)
    print (f'your username is: {username}')
    
def create_password():
    password = input("enter password: ")
    print(f'your password is: {password}')

def user_info():
    pass

def exit_program():
    print("Goodbye!")
    exit()
