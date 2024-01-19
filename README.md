# Phase 3 Project

Creators: Steven Mentzer, Igor Rakush, Tyler Kim

## App Description
An interface to quickly design and schedule art exhibitions and track an artworks location.

## Model Classes
- Owner
- Art 
- Museum
- Exhibition

## Domain Model Table
View draw.io file

## CRUD 
- Create: 
    - User 'Role' objects as 'Museum' or 'Owner'
    - 'Museum's can create new 'Exhibition's
- Read: 
    - 'Musuem' and 'Owner' can access data on exhibtions and art objects 
- Update: 
    - 'Musuem' and 'Owner' change dates on exhibtions
    - 'Owner' can change the art value
- Delete: 
    - Cancel an exhibition
## Functionality
1. The user chooses their role: Owner, Musuem.
2. Choose from existing user or make a new one.
3. Interact with data TBD


## Extra Functions
Musuem:
- Request art for an exhibtion (start_date & end_date).
- Create exhibitions with multiple artworks
- Get a list of all exhibitions museum
- Get a list of all artwroks in museum


Owner:
- Approve loan requests.
- View their art object data
- Get art location 
- Get number of times its been shown

---

## Files 
### cli.py

### helpers.py

## What Goes into a README?

This README serves as a template. Replace the contents of this file to describe
the important files in your project and describe what they do. Each Python file
that you edit should get at least a paragraph, and each function should be
described with a sentence or two.

Describe your actual CLI script first, and with a good level of detail. The rest
should be ordered by importance to the user. (Probably functions next, then
models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.
