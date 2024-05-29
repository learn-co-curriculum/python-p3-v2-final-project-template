# Blogger CLI+ORM Project

This a a group project that was created by Dan Jacoby and Grant Cummings to showcase our skills we have aquired learning how to interact with a database. The project uses Python along with SQL commands to interact with a sqlite3 database. As a user you will be able to do the following:

## User Stories:

* As a user, I would like to create Blog Posts linked to a specific author
* As a user, I would like to link each post to a specific category
* As a user, I would like to view all Authors
* As a user, I would like to find an author by their ID
* As a user, I would like to find an author by their name
* As a user, I would like to view posts by a specific author
* As a user, I would like to view all posts by all authors
* As a user, I would like to view all posts by a specific category
* As a user, I would like to know how many posts a specific author has created
* As a user, I would like to edit an existing user's name
* As a user, I would like to edit an existing post
* As a user, I would like to delete an author and all the posts linked to that author
* As a user, I would like to delete a specific post

## Requirements:

* User should be able to exit the terminal from the main menu
* When creating an authors name, name  must by a string and between 1 and 15 characters
* When creating a new post, user must link the post to an existing author
* If no author exists, user will be prompted to create an author
* For each post, a title must be given and be between 1 and 20 charachters
* For each post, a category must be linked from a list of given categories
* For each post, the user must enter content for the post
* If the user doesn't want to add an author or post, they should be able to navigate back to the main menu
* When searching for author related content, if the author doesn't exist, it should error out
* If the user doesn't want to view author or post related content, they should be able to navigate back to the main menu
* For editing authors, if there are no authors to edit, it should bring the user back to the edit menu
* For editing posts, if there are no posts to edit, it should bring the user back to the edit menu
* If the user doesn't want to edit author or post, they should be able to navigate back to the main menu
* When deleting an author, both the author and the related posts should be deleted
* If the user doesn't want to delete an author or post, they should be able to navigate back to the main menu



## Create authors and posts to be persisted to a relational database backend, all within the CLI!

* Initially choose between a set of options to redirect you to 4 different types of menus that have to do with create, read, update and deleting authors or posts
* Create authors to be intialized with a name and favorite category
* Create posts to be initialized with a title, content, category and author id
* Find authors by name or id from database
* Find posts by title or id from database
* View all authors
* View all posts
* View all posts by a specific author 
* View all posts by a specific category
* View number of posts by an author
* Update authors and posts
* Delete authors and posts
* Exit the program

## How to install and use this application in your local computer

1. Fork and clone the repo to a repository within your GitHub.
2. Open the project in your code editor of choice (ours is VS Code)
3. In your terminal within the the project's folder run "$ pipenv install" to install all dependencies for the project
4. Run "$ pipenv shell" to create a shell environment to use the program
5. Run "$ python lib/cli.py" to use the program within your terminal


## Final note
This is a backend only project and would work much better if there was a frontend when it comes to the amount of posts that can be generated. This project is a representation of the skills we have when interacting with the database of a program. 