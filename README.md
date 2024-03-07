# Phase 3 Concerts-CLI Group Project

## Introduction

Eve, Ikram and Kenny are building a one to many relationship with one concert having many bands and one city.  This project will help the user find information about a concert or band to see where and when events will take place.  We are also giving the ability to the user to create, delete, update any concert or band at any time.  They can also find the concerts and bands by id, or name.  We are using Python and SQL for our coding.


```VS Code model:
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── band.py 
    |   └── city.py 
    |   └── concert_band.py
    |   └── concert.py
    |   └── seed.py
    |   └── utils.py
    |   
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── main.py
```

Our project will let the user:
    Perform CRUD operations on bands and concerts.
    See all of the concerts in a city.
    See all bands and concerts.
    See all members of band (just strings).
    See genres of bands at a concert.
    See the pricing per ticket at a concert.
    See if the band is playing in their home city.
    Reset (reseed) the table at the user's discretion. 
    See a well laid out format in the terminal to help the user navigate the menu.

Our stretch goals we will try to add:
    Graphs:
    Attendance with ticket type/price at the concert.
    Attendance per genre over all concerts.
    Coordinates to show the concerts on a map with additional data: number of attendance (by the size of a dot).
    Show the band's concerts based on current date.

We will implement SQL and use Python methods to insert logic to the inputs from the user.
There are imports from class to class to pull needed information.