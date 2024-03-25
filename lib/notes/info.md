# Project MVP:

## Classes
- [ ] Posts - can have a Task
- [ ] Tasks - each task will have a Post and a Reviewer
- [ ] Reviewer - will have a list of Tasks (which points to the Post)


## Method: 
- [ ] once a post reaches viral status, a Task is created and assigned a Reviewer


## CLI: For each user(Reviewer) can:
- [ ] create an object
- [ ] delete an object 
- [ ] display all objects 
- [ ] view related objects 
- [ ] find an object by attribute
- [ ] status -fact needs to be checked, in progress, or has been checked
- [ ] update - add a note: factual vs not
- [ ] If factual: post get a badge of being Verified
- [ ] If not factual: gets a badge of being Debunked
- [ ] Badge = attribute which lives in the post, but updated through the Task


## Stretch:
- [ ] After the post is reviewed and is found to be false, then figure out what action should be taken?
- [ ] Possible warning to the account who posted
- [ ] Create a status for items that have been reviewed but was not able to determine if factual or not
- [ ] Third badge? Proceed with caution
- [ ] Each reviewer can assign priority to tasks on their task list 
- [ ] Priority levels: low, medium, high, blocker (all hands on deck)


## Rough Schedule
- [x] Fill out Project Pitch
- [x] Repo set up
- [x] Classes and methods
- [ ] db built
- [ ] Layout db Schema
- [ ] Recommend to check your DB FIRST, to ensure your data structure will work! 😉
- [ ] Seeding db from seed.py
- [ ] SQL queries
- [ ] Start building the CLI
- [ ] CLI class and logic


Monday
- [ ] MVP done


Tuesday
- [ ] Clean up code
- [ ] Work on stretch goals
- [ ] ReadMe



# One sentence app description:
Fact checking queue, triggered by a post becoming viral. An internal tool for platform owners to mitigate disinformation.



# Requirements
You need to implement a Python CLI Application that meets the following requirements.

ORM Requirements
- [x] The application must include a database created and modified with Python ORM methods that you write.
- [x] The data model must include at least 2 model classes.
- [x] The data model must include at least 1 one-to-many relationship.
- [ ] Property methods should be defined to add appropriate constraints to each model class.
- [ ] Each model class should include ORM methods (create, delete, get all, and find by id at minimum).

CLI Requirements
- [ ] The CLI must display menus with which a user may interact.
- [ ] The CLI should use loops as needed to keep the user in the application until they choose to exit.
- [ ] For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- [ ] The CLI should validate user input and object creations/deletions, providing informative errors to the user.
- [ ] The project code should follow OOP best practices.
- [ ] Pipfile contains all needed dependencies and no unneeded dependencies.
- [ ] Imports are used in files only where necessary.
- [ ] Project folders, files, and modules should be organized and follow appropriate naming conventions.
- [ ] The project should include a README.md that describes the application.
- [ ] You do not need to implement tests for pytest, although you should test your code thoroughly using your CLI. Try entering bad data when prompted for input, and confirm your application prints a useful error message.
  
This is a summary of the project requirements and inherently also the parameters I will use to evaluate your projects:

- [ ] a cli (command line interface) with a database (sqlite3 adapter)
- [x] at least 2 tables with a one-to-many relationship (I would love to see a many-to-many though 🤓) manual ORM to implement: create, delete, get all, and find by id at minimum
- [ ] For EACH class in the data model, the CLI must include options: to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
- [ ] well-organized code (separate classes for separate responsibilities) respect OO principles (SST, SOC, SOLID)
- [ ] seeding the database can happen from an api call, using faker or even manually you might scrape pages or make API calls to enrich your CLI
- [ ] feel free to use Click(https://click.palletsprojects.com/en/8.1.x/) or Fire(https://google.github.io/python-fire/guide/) to boost your CLI if you’d like
- [ ] Make sure your program validates EVERY user input and handles incorrect values accordingly
- [ ] Make sure your CLI has the option to quit/exit the program at any point and it doesn’t break on its own otherwise
- [ ] Pipfile contains all needed dependencies and no unneeded dependencies.
- [ ] Imports are used in files only where necessary.
- [ ] Project folders, files, and modules should be organized and follow appropriate naming conventions.
- [ ] The project should include a README.md that describes the application.


## Tips and Tricks?
- Think about your database schema before you begin- migrations are a pain!
- Keep your Python objects, sqlite3 objects, and CLI script in separate modules.
- If you get stuck trying to accomplish a specific task, check online to see if there's a Python library that will make it easier.
- Consider using ClickLinks to an external site. or FireLinks to an external site. to take care of basic CLI tasks for you.


# Starting on the project - possible flow:
- [x] Pitch Prep (ERD/UML class/table diagram, timeline, core and stretch deliverables)
- [x] Start with the project template (provided in the following lesson). You are free to adapt the template structure, as long as you adhere to the project requirements.
- [ ] Class basic creation along with init, create_table(), drop_table(), create(), save().
- [ ] Work on seeding the db from inside your seed.py file using the class methods create() and the instance method save(). Feel free to seed the db with Faker, manually, or fetching/scraping data from the internet.
- [ ] Start equipping your classes with a few utility methods you know you will need (find_by(), find_or_create_by(), delete(), update(), etc)
- [ ] Start building the direct and through association methods (in case of a many-to-many) or only the direct association method (in case of a one-to-many). 
- [ ] Think about the user interaction. How will you prompt the user? What information will the user enter? How will you provide feedback to the user?
- [ ] Think about your data model. How will you organize and store the information received from the user?
- [ ] Start on the CLI class, what should be the flow for your for loop? What will be the main program options?
- [ ] Start forming CLI logic leveraging the other classes methods and VALIDATE EVERYTHING. Ensure that you are ACTUALLY USING the all the associations methods in your program.


## Advice to listen to closely
- [ ] You should always test your CLI by passing wrong values for ALL inputs and see what happens!
- [ ] The project revolves around many things but a MAJOR one are associations. Please make sure you actually build association methods AND USE THEM in the app. In a Doctor -> Appointment <- Patient example, given a doctor's name I allow the cli to list all the appointments AND all of the patients connected to the appointments.



## Links
[Pitch](https://docs.google.com/document/d/1Z9TDApNsv47NTMtcne-6JzDvuNjWAy22y7ab85noH0I/edit)

[Figma](https://www.figma.com/file/fhEHaljiHTu1Ggq4MauxM9/Ticket-Triage?type=whiteboard&node-id=1-143&t=B0Ju54tsqe1MpQus-0)

[Agreements](https://docs.google.com/document/d/1dPnwGhVtD0gjsfksEX_U1fX0R6dR-xWXKnOaCmjHyZU/edit#heading=h.e33dnqfb92rb)


[Project Requirements](https://learning.flatironschool.com/courses/7237/pages/phase-3-project-cli?module_item_id=655050)

[Grading Rubric](https://learning.flatironschool.com/courses/7237/assignments/271873?module_item_id=655054)
