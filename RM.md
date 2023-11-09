Welcome to Adventures of your choice

To start the program the user will need to type in the command line:
     
     python lib/cli.py  

Here the user will see a menu that displays the choices.
From there they can choose to login or start with world or player options.
If the user decides to play later they can choose to exit.

Our user can communicated with the data base by creating, reading, upating, and deleting. 
We do have some restrictions and if the user chooses something not with in the boundaries we have set a error is raised informing the user of the restriction. 

World Option

1. Create World:
 When creating a world the user can name their world as long as it is a string and 1 - 15 characters
 long. If the user steps out the set boundaries a messasge is printed "print("Please Enter A Shorter Name")".
2. Display Worlds:
Will display a list of created worlds the user can choose from. Once the user sees the list of world they can selete a world by typing its id number.
3. Delete World: 
To delete a world the user can type in it id and the world will be removed. 

Player Menu

1. Display Players:
  / __|| |_   ___  ___  ___ ___   _  _  ___  _  _  _ _   / __|| |_   __ _  _ _  __ _  __ | |_  ___  _ _ 
 | (__ | ' \ / _ \/ _ \(_-</ -_) | || |/ _ \| || || '_| | (__ | ' \ / _` || '_|/ _` |/ _||  _|/ -_)| '_|
  \___||_||_|\___/\___//__/\___|  \_, |\___/ \_,_||_|    \___||_||_|\__,_||_|  \__,_|\__| \__|\___||_|
  The user can create their character by typing in a name that is a string and the character length of 1-10. If the user steps out the set boundaries a messasge is printed "print("Please Enter A Shorter Name")".
2. Display Players's 
The user can see a list of created characters for the user to choose from. Once the user can selete from the list by typing in the players id.
3. Remove Player
To delete a player the user can type in its id and the player will be removed. 
4. find Player by name
The user can search for a player by name. They program is cap and space sensitive.
5. Login A player to a world
If the player knows their world id of choice they may login their player in that way as well.
6. Search a Player Worlds
The user can search for a world by name. They program is cap and space sensitive

In each menu we do have a way to return to the previous menu. 







