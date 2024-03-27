import click
from rich import print
from rich.prompt import Prompt
import random

from cli.pages import (
    define_page,
    navigate,
    go_back,
    draw_page,
    handle_user_input,
    exit_program,
    pages,
    current_page,
    previous_pages,
)
from cli.user_account_page import user_account_page
from cli.restaurants_page import restaurants_page
from cli.visits_page import visits_page


from cli.view_all_restaurants import display_restaurants

from classes.User import User
from classes.Restaurant import Restaurant



###############################################
#   ______      __                            #
#  /_  __/___  / /____  ______                #
#   / / / __ \/ //_/ / / / __ \               #
#  / / / /_/ / ,< / /_/ / /_/ /               #
# /_/_______/_/|_|\__, /\____/                #
#   / __ \____ _________ _/ /______ _________ #
#  / / / / __ `__ \/ __ `/ //_/ __ `/ ___/ _ \#
# / /_/ / / / / / / /_/ / ,< / /_/ (__  )  __/#
# \____/_/ /_/ /_/\__,_/_/|_|\__,_/____/\___/ #
###############################################

#⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⠿⠟⣻⡿⢻⡿⢷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠋⠀⣠⡾⣫⡾⠋⠀⠀⠀⠉⠛⠿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠁⢀⡾⢋⡴⠋⠀⠀⠀⠀⠀⠀⢀⣴⠟⢩⡿⢿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⣠⣿⣯⣿⠏⢀⣴⢏⡴⠋⠀⠀⠀⠀⠀⣀⣠⠶⢛⣡⡶⠋⠀⠀⠈⠛⢿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⣠⣾⢟⣵⣿⠋⣠⢞⣵⠟⠁⠀⠀⣀⣤⠴⣛⣩⡴⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⢛⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣴⣿⢟⣡⣿⡿⠁⣴⢫⠞⠁⠀⣠⠶⣛⣭⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⡴⠟⠁⣽⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⣿⡵⢟⠷⠋⢀⣾⣷⣿⢿⡟⣛⣻⢿⣧⣤⣀⣤⡴⠖⠒⠛⠛⠉⠀⠀⠉⣉⣉⣉⣀⣠⡤⠞⠁⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠙⠻⠷⠶⠟⠛⠉⠸⣷⡄⠉⠉⠙⣧⡬⢽⡻⣷⣖⡛⠛⠋⠉⠉⠉⠈⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠸⣿⣤⡀⠀⠀⠀⠀⠈⠓⠺⡟⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣤⡀⠀⠀⠀⠀⠀⠛⠲⢿⣿⣶⣤⣤⣤⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣿⡆⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⡀⠀⠀⠀⠀⠈⠷⠭⣿⣷⣤⣤⣄⣀⣉⠉⠙⠛⠒⠶⠦⠤⠤⠶⠛⢁⣸⣿⡀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠹⣷⣾⣧⠀⢀⡀⠀⠀⢸⣙⣻⣷⡀⠈⠉⠉⠙⠛⠓⠒⠒⠶⠶⠶⠚⠋⠁⢻⣇⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣧⣀⣀⣀⢼⣃⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢿⣤⣿⣷⣤⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⢿⣦⡀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠉⠉⠁⠙⣿⣏⠛⠲⠦⣤⣀⣀⢀⣀⣠⠟⢀⡼⠛⢿⣦⣄⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣟⠲⠦⢬⣭⣉⣉⣠⡴⠛⠁⠀⠀⠉⠻⢿⣦
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣷⣦⣀⠀⠀⠀⠀⢀⣴⣾⠟⠋⠁
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤⣴⡿⠋⠀⠀⠀⠀


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣤⣤⣤⣤⣤⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠛⢻⠛⢻⠛⢻⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⡿⠀⣼⠀⢸⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⣿⠀⢹⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⡀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠸⡆⠘⣇⠀⢿⣷⠀⠀⠀⠀⣀⣠⣤⣶⣶⣾⣿⠿⠿⠛⠋⢻⡆
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⣿⠀⢿⣄⣸⣿⣦⣤⣴⠿⠿⠛⠛⠉⠁⢀⣀⣀⣀⣄⣤⣼⣿
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⡿⠀⣼⣿⣿⣯⣿⣦⣤⣤⣶⣶⣶⣿⢿⠿⠟⠿⠛⠛⠛⠛⠋
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⣸⠃⢠⡟⢻⣿⣿⣿⣿⣿⣭⣭⣭⣵⣶⣤⣀⣄⣠⣤⣤⣴⣶⣦
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⣿⠀⣸⠀⢸⣿⣶⣦⣤⣤⣄⣀⣀⣀⠀⠀⠉⠈⠉⠈⠉⠉⢽⣿
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣿⡇⠀⣿⠀⢸⠀⢸⣿⡿⣿⣿⣿⣿⡟⠛⠻⠿⠿⠿⣿⣶⣶⣶⣶⣿⣿
# ⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⡿⣿⣿⣿⣷⠀⠹⡆⠘⣇⠈⣿⡟⠛⠛⠛⠾⣿⡳⣄⠀⠀⠀⠀⠀⠀⠈⠉⠉⠁
# ⠀⠀⠀⠀⠀⠀⣰⣿⢟⡭⠒⢀⣐⣲⣿⣿⡇⠀⣷⠀⢿⠀⢸⣏⣈⣁⣉⣳⣬⣻⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⣀⣤⣾⣿⡿⠟⠛⠛⠿⣿⣋⣡⠤⢺⡇⠀⡿⠀⣼⠀⢸⣿⠟⠋⣉⢉⡉⣉⠙⠻⢿⣯⣿⣦⣄⠀⠀⠀⠀
# ⢠⣾⡿⢋⣽⠋⣠⠊⣉⠉⢲⣈⣿⣧⣶⣿⠁⢠⣇⣠⣯⣀⣾⠧⠖⣁⣠⣤⣤⣤⣭⣷⣄⠙⢿⡙⢿⣷⡀⠀⠀
# ⢸⣿⣄⠸⣧⣼⣁⡎⣠⡾⠛⣉⠀⠄⣈⣉⠻⢿⣋⠁⠌⣉⠻⣧⡾⢋⡡⠔⠒⠒⠢⢌⣻⣶⣾⠇⣸⣿⡇⠀⠀
# ⣹⣿⣿⣷⣦⣍⣛⠻⠿⠶⢾⣤⣤⣦⣤⣬⣷⣬⣿⣦⣤⣬⣷⣼⣿⣧⣴⣾⠿⠿⠿⢛⣛⣩⣴⣾⣿⣿⡇⠀⠀
# ⣸⣿⣟⡾⣽⣻⢿⡿⣷⣶⣦⣤⣤⣤⣬⣭⣉⣍⣉⣉⣩⣩⣭⣭⣤⣤⣤⣴⣶⣶⣿⡿⣿⣟⣿⣽⣿⣿⡇⠀⠀
# ⢸⣿⡍⠉⠛⠛⠿⠽⣷⣯⣿⣽⣻⣻⣟⢿⣻⢿⡿⣿⣟⣿⣻⢟⣿⣻⢯⣿⣽⣾⣷⠿⠗⠛⠉⠁⢸⣿⡇⠀⠀
# ⠘⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠛⠙⠛⠛⠛⠛⠋⠛⠋⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣿⡿⠀⠀⠀
# ⠀⠹⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣦⡀⠀⠀⠀⠀⠀⠀⣼⣿⠇⠀⠀⠀
# ⠀⠀⠹⣿⣆⠀⠀⠀⠀⠀⠀⠀⠻⠿⠟⠀⠀⠀⠿⣦⣤⠞⠀⠀⠀⠻⠿⠟⠀⠀⠀⠀⠀⢀⣼⣿⠋⠀⠀⠀⠀
# ⠀⠀⠀⠘⢿⣷⣶⣶⣤⣤⣤⣀⣀⣀⡀⣀⠀⡀⠀⠀⠀⡀⣀⡀⣀⣀⣀⣠⣤⣤⣴⣶⣶⣿⡿⠃⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠙⢿⣿⣾⡙⠯⠿⠽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠙⢋⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣾⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⠙⠻⠿⡿⠷⠶⡶⠶⠶⠶⠶⠶⣾⢿⣿⢿⠛⣉⣡⠀⠀⠀


# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠋⠉⣿⣤⣤⡾⠏⠛⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣳⣿⠡⣠⣄⣚⣿⡟⣗⡄⠐⣈⣻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⣀⠛⢋⡿⢻⡿⢻⠟⠁⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠉⠉⠉⠉⠓⠶⣶⠲⠖⠒⠛⠒⠛⠒⠓⠓⠒⠒⠒⠶⠿⠶⣿⣿⣶⡿⢁⣾⣿⣄⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⢀⣠⣴⡟⠀⠀⠀⠀⣀⣤⣄⣀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⢁⡾⠛⢿⠿⣧⣄⡉⠀⠈⠿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⢀⣠⡴⠚⠉⣽⠃⠀⠀⢀⡴⠋⠉⠉⠙⢦⡀⠹⣦⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⣀⡴⠋⣠⠞⠁⠀⠈⠀⠉⠙⠳⣦⣀⠠⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⢀⣴⠛⠁⠀⠀⢀⣿⢀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢳⠀⠹⣇⠔⡁⠀⣰⠌⢀⣈⣭⠿⠛⢉⣴⣾⣷⣤⣄⣀⡀⠀⠀⠀⠀⠀⠙⢷⣟⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀
# ⢀⡿⠁⠀⠀⠀⣠⡼⣷⠸⡄⠀⠉⢷⡀⠀⠀⠀⢀⡼⠀⠀⣿⢀⣉⣷⡶⠿⢿⣏⣤⠶⣿⣿⡽⣶⣭⣉⠻⣯⡙⠳⢤⣀⠀⠀⠀⠀⢹⣾⣧⠀⠀⠀⠀⠀⠀⠀⠀
# ⢸⡇⠀⠀⣠⢾⡟⠂⢻⡆⢳⣄⡀⠀⠙⠶⠤⠴⠛⠡⠔⢻⣿⣻⣿⡴⠶⠛⢻⣏⣡⣾⠿⠷⣤⣦⣴⣽⣷⣞⢿⡌⠘⢏⢳⣄⠀⠀⢀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀
# ⠈⣷⡄⢰⡏⠰⠓⢠⡴⠿⡾⠿⢷⡀⠀⠀⠀⠀⠀⠀⣠⣾⣟⣿⡌⣷⣤⣴⡿⢛⣩⡴⠶⠳⣿⠿⢿⣿⠾⣿⡟⠋⠁⠀⠲⢽⡆⢀⣼⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⣿⣿⣶⣿⣄⠀⠸⣧⣀⣀⣀⣽⣟⣶⠶⡶⢶⣶⣫⣿⣋⣉⣙⣿⠌⣿⢷⡿⢻⡇⠀⠀⠀⠘⣻⠶⣶⠾⠟⢹⠆⠀⠀⢀⣼⣷⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⢻⡌⠻⢿⣿⣷⣶⣬⣍⢻⣏⠻⣿⣟⠻⠿⢛⣻⣧⣌⣉⣉⣭⠟⢠⣿⡐⢿⣆⠻⣦⣀⣀⣴⠟⣠⡟⠀⢀⣀⣤⣴⣾⣿⣿⠟⢁⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⢿⣦⣀⠉⠛⠿⣿⣻⣿⣿⠷⢿⣿⣿⣽⣟⣻⣤⣉⣛⣫⣥⡀⢀⣸⣇⣼⣟⣶⣤⣭⣭⣴⣾⣿⠶⢿⢛⣏⣹⡴⠛⠁⢀⣴⣾⠿⣿⣟⣷⣦⠀⠀⠀⠀⠀⠀
# ⠀⠀⠈⣿⣿⣿⣶⣤⣀⡈⠉⠛⠛⠶⠶⣦⣭⣎⣭⣋⣟⣙⣛⣛⣻⣛⣛⣛⣏⣻⣍⣯⣭⣱⡶⠶⠿⠓⠛⠋⠉⣀⡄⠀⣠⣟⣾⠃⠀⠈⠙⠛⠁⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠈⠻⣿⣷⢯⡿⣽⢿⣶⣶⡲⣤⠤⣄⣀⣀⣁⣈⣉⡉⠉⠁⠉⠉⠉⣈⣁⣈⣀⣀⣀⡤⣤⠴⣲⠒⣏⣿⠏⠀⡴⣧⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠙⢿⣿⣽⣻⣟⣮⣟⣷⡌⢳⡘⢬⢲⡡⢎⠭⣙⠏⢯⡹⢭⡙⢥⠚⡔⡣⣜⢡⠞⣠⢛⡤⢯⡴⢬⡷⣞⣷⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠙⢷⣿⣟⣾⡽⣾⢿⡆⡝⣆⠣⡜⣡⢋⢆⡛⢦⠱⢦⡙⢦⠛⣬⠱⡌⠮⡜⢥⣋⡜⢯⣤⣞⣵⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣯⣿⣯⣟⣿⣶⣌⠳⡜⢤⢋⠦⡙⢦⡙⠦⡙⢦⠹⢤⠓⣍⠞⡸⢆⡱⢎⣽⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠛⠻⣿⣾⣿⣷⣯⡘⢣⠞⡲⢩⠦⣙⠲⣍⠲⡙⢦⡙⢦⣩⣵⣾⠿⡟⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡄⠠⠰⠘⢿⣿⣿⡿⣿⣷⣮⣵⣧⣾⣤⣷⣬⣧⣽⣶⣿⣿⣿⣿⠃⢃⠀⠂⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣄⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣍⡀⠂⠌⠛⢿⣿⣿⣿⣽⣯⣿⣽⣯⣿⣽⣿⣽⣷⣿⠿⠋⠡⠈⠁⠈⠼⠃⢀⣀⣠⣤⠤⠶⠶⠚⠛⠋⠉⠉⠀⠀⣐⣿⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⠦⣔⣀⠊⠉⠉⠛⠛⠛⠿⠻⠟⠟⠻⠛⠛⠩⠙⣀⣂⣤⣤⣶⠶⠶⠒⠚⠋⠉⠉⠀⠀⢀⣀⣀⣴⣤⣶⠶⠶⢿⡟⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠉⠐⠀⠉⠐⢠⣥⣬⣭⠶⠷⠞⠛⠋⠉⠉⣀⣀⣀⣠⣒⣤⣥⣬⠶⠶⢿⠛⠻⠭⠉⠁⠀⠀⠈⠉⠀⣀⣀⣤⡀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⡤⠤⠶⠒⠛⠋⢉⠉⣁⣀⣠⣤⣤⣴⠶⠾⠾⠟⠛⠛⠙⠉⠉⠀⠀⢀⣀⣀⣠⣤⠤⠤⠶⠖⠚⠛⠛⠉⠉⠉⠁⢀⣿
# ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⠛⠛⠉⢉⣀⣀⣠⣤⣤⣴⠶⠾⠛⠛⠛⠉⠉⠀⠀⣀⣀⣀⣤⣤⡤⠶⠶⠖⠚⠛⠋⠉⠉⠁⠀⢀⣀⣠⣤⣠⣤⣤⣤⡶⠶⠿⠟⣛⡏
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠶⠛⠛⠋⠉⠉⣁⣀⣀⣄⡤⡤⠤⠶⠖⠒⠚⠛⠉⠉⢉⡀⣀⣀⣠⣤⣤⣤⣴⠶⠶⠷⠟⠾⠛⠛⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠖⠚⠛⠉⠉⠉⣁⣀⣤⣄⣠⣤⣤⣴⠶⠶⠶⠛⠛⠛⠋⠙⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

@click.command()
def main():
    # Welcome User

    while True:

        click.clear()
        current_users = [user.name for user in User.get_all()]

        print('''###############################################
#   ______      __                            # 
#  /_  __/___  / /____  ______                #
#   / / / __ \/ //_/ / / / __ \               #
#  / / / /_/ / ,< / /_/ / /_/ /               #
# /_/_______/_/|_|\__, /\____/                #
#   / __ \____ _________ _/ /______ _________ #
#  / / / / __ `__ \/ __ `/ //_/ __ `/ ___/ _ \#
# / /_/ / / / / / / /_/ / ,< / /_/ (__  )  __/#
# \____/_/ /_/ /_/\__,_/_/|_|\__,_/____/\___/ #
###############################################''')
        
        print('\n[white]Welcome to[/white] [#FF7EF5]TOKYO OMAKASE [/#FF7EF5]\n')
        print('\n[#FF7EF5]東京のお任せ[/#FF7EF5][white]へようこそ！[/white] \n')

        choice = click.prompt('Login or Create New User? (l/n)').lower()

        if choice == 'l':
            login_name = click.prompt('\nEnter User Name')
            if login_name in current_users:
                User.set_current_user(User.get_user_by_name(login_name))
  
                print('[green]\nLogin Successful!\n[/green]')
                click.pause()            
                break;
            else:
                print('\n[red]Please enter an existing username[/red]\n')
                click.pause()

        elif choice == 'n':
            new_user = click.prompt('\nEnter New User Name')
            if new_user in current_users:
                print('[red]\n\nName already in use...\n\nPlease pick a different name\n\n[/red]')
                click.pause()
            else:
                if not (len(new_user) > 0 and len(new_user) <= 12):
                    print('\n[red]Please enter a valid input between 1 and 12 characters[/red]\n')
                    click.pause()
                else:

                    User.set_current_user(User.create(new_user))

                    print(f'[green]\nNew User \"{new_user}\" created\n\nLogging in...\n[/green]')
                    click.pause()   
                    break

        else:
            print('\n[red]Please enter a valid input[/red]\n')
            click.pause()


    def omakase_restaurant():
        click.clear()
        rest_length = len(Restaurant.get_all())
        randomizer = random.randint(0,rest_length)

        random_restaurant = Restaurant.get_by_id(randomizer)

        while True:

            print('[white]=[/white]' * 20)
            print(f'\n[#FF7EF5]{random_restaurant.name}[/#FF7EF5]\n')
            print(f'\n[white]{random_restaurant.description}[/white]\n')
            print(f'\n[#FF7EF5]Location:[/#FF7EF5] {random_restaurant.address}\n')
            print(f'[#FF7EF5]Cuisine:[/#FF7EF5] [blue]{random_restaurant.cuisine}[/blue]\n')
            print(f'[#FF7EF5]Price:[/#FF7EF5] [blue]{random_restaurant.price}[/blue]\n')
            print(f'[#FF7EF5]Award:[/#FF7EF5] [blue]{random_restaurant.award}[/blue]\n')
            print('[white]=[/white]' * 20)
            print('\n')

            choice = Prompt.ask('Press \'x\' to return home')
            if choice == 'x':
                navigate('home')
                break
            else:
                click.clear()
            



    # Define pages
    home_page = define_page("home", "Home")
    home_page.add_option("Restaurants", lambda: navigate("restaurants"))
    home_page.add_option("My Visits", lambda: navigate("visits"))
    home_page.add_option("お任せします！ (view a random restaurant)", lambda: omakase_restaurant())
    home_page.add_option("Manage Users", lambda: navigate("user_account"))


    view_all_restaurants_page = define_page("view_all_restaurants", "All Restaurants")
    view_all_restaurants_page.add_option("Display Restaurants", lambda: display_restaurants(1))
    view_all_restaurants_page.add_option("Back", lambda: navigate("restaurants"))

    navigate("home")

    while True:
        draw_page()
        user_input = click.prompt("Enter your choice").lower()
        handle_user_input(user_input)

if __name__ == "__main__":
    main()