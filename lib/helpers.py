# lib/helpers.py
from classes.reviewer import Reviewer
from classes.post import Post
from classes.task import Task

def exit_program():
    print("Goodbye!")
    exit()

#Reviewer
def list_reviewers():
    reviewers = Reviewer.get_all()
    for reviewer in reviewers:
        return reviewer
    
def find_reviewer_by_id():
    id_ = ("Enter the reviewer's id: ")
    reviewer = Reviewer.find_by_id(id_)
    print(reviewer) if reviewer else print(f'Reviewer {id_} not found')

def create_reviewer():
    id = input("Enter the reviewer's id: ")
    name = input("Enter the reviewer's name: ")
    try:
        reviewer = Reviewer.create(id, name)
        print(f'Success: {reviewer}')
    except Exception as e:
        return e

def update_reviewers():
    id_ = input("Enter the reviewer's id: ")
    if reviewer := Reviewer.find_by_id(id_):
        try:
            name = input("Enter the reviewer's new name: ")
            reviewer.name = name

            reviewer.update()
            print(f'Success: {reviewer}')
        except Exception as e:
            return e
    else:
        print(f'Reviewer {id_} not found')

def delete_reviewer():
    id_ = input("Enter the reviewer's id: ")
    if reviewer := Reviewer.find_by_id(id_):
        reviewer.delete()
        print(f'Reviewer {id_} deleted')
    else:
        print(f'Reviewer {id_} not found')

#Post
def list_posts():
    posts = Post.get_all()
    for post in posts:
        return post

def find_post_by_id():
    id_ = input("Enter the post's id: ")
    post = Post.find_by_id(id_)
    print(post) if post else print(f'Post {id_} not found')

def create_post():
    pass

def update_post():
    pass

def delete_post():
    pass
#Task
def list_tasks():
    pass