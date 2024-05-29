# lib/helpers.py
from models.author import Author 
from models.post import Post



#def helper_1():
#    print("Performing useful function#1.")



def exit_program():
    print("\nBlogger says Goodbye!\n")
    exit()

#? Adding features
def add_author():
    try:
        author = input("Author name: ")
        favorite_category = input(f"Choose favorite category from list of categories {Post.categories}: ")
        while favorite_category not in Post.categories:
            print("Invalid Category")
            favorite_category = input(f"Choose favorite category from list of categories {Post.categories}: ")
        Author.create(author, favorite_category)
        print(f"\nAuthor {author} added successfully.")
    except Exception as exc:
        print(f"\nError: {exc}")

def write_post():
    from cli import create_menu
    author_ids = [f"{object.id}: {object.name}" for object in Author.get_all()]
    if len(author_ids) > 0:
        author_id = input(f"Enter an author id from this list {author_ids}: ")
        while author_id not in [str(object.id) for object in Author.get_all()]:
            print("name not in list")
            author_id = input(f"Enter an author id from this list {author_ids} ")
        title = input("Enter a title: ")
    else:
        print("\nNo authors found. Must add an author first.")
        create_menu()

    category = input(f"Enter a category from list of categories {Post.categories}: ")
    while category not in Post.categories:
        print("invalid category")
        category = input(f"Enter a category from list of categories {Post.categories}: ")
    content = input("Post content: ")
    Post.create(title, content, category, author_id)
    print("\nPost created successfully!")
    

    
#? Viewing features
def view_authors():
    authors = Author.get_all()
    if authors:
        for author in authors:
            print(f"\n-{author.name}- Favorite Category: {author.favorite_category} id: {author.id}")
    else :
        print("\nNo authors found")

def find_number_of_posts_by_author():
    authors = [f"{author.id}: {author.name}" for author in Author.get_all()]
    id_ = input(f"Input author's id to see number of posts. {authors}: ")
    try:
        author = Author.find_by_id(id_)
        authors_posts = author.find_all_posts()
        post_plural = "post" if len(authors_posts) == 1 else "posts"
        print(f"\nAuthor {author.name} has {len(authors_posts)} {post_plural}.")
    except Exception as exc:
        print(f"\nAuthor not found. {exc}")
        
            
def find_author_by_id():
    id_ = input("Enter the author's id: ")
    author = Author.find_by_id(id_)
    if author:
        print(f"\nAuthor Found: -{author.name}- Favorite Category: {author.favorite_category} id: {author.id}")
    else: 
        print(f"\nAuthor {id_} not found")
        

def find_author_by_name():
    name = input("Enter the author's name: ")
    author = Author.find_by_name(name)
    if author:
        print(f"\nAuthor Found: -{author.name}- Favorite Category: {author.favorite_category} id: {author.id}") 
    else:
        print(f'\nAuthor {name} not found')

def view_authors_posts():
    author_id = input("Enter the author's id: ")
    author_object = Author.find_by_id(author_id)
    if author_object:
        posts = author_object.find_all_posts()
        if not posts: print(f"\nAuthor {author_object.name} has no posts yet")
        try:
            for post in posts:
                print(f"\nTitle: {post.title} || Category: {post.category} || {post.content}")
        except Exception as exc:
            print("Error finding posts: ", exc)
    else :
        print(f"\nAuthor id of {author_id} not found")
    

def view_all_posts():
    posts = Post.get_all()
    if posts:
        for post in posts:
            author = Author.find_by_id(post.author_id)
            print(f"\nTitle: {post.title} || Category: {post.category} || Author: {author.name} || {post.content}")
    else :
        print("\nNo posts found")

def view_posts_by_category():
    category = input(f"Enter a category from the list {Post.categories}: ")
    posts = Post.find_by_category(category)
    if posts:
        for post in posts:
            author = Author.find_by_id(post.author_id)
            print(f"\nTitle: {post.title} || Author: {author.name} || {post.content}")
    else :
        print(f"\nCategory {category} has no posts")
        


#? Edit features
def edit_author():
    author_ids = [f"{object.id}: {object.name}" for object in Author.get_all()]
    if len(author_ids) > 0:
        author_id = input(f"Enter an author id from this list {author_ids} ")
        while author_id not in [str(object.id) for object in Author.get_all()]:
            print("Author id is not in list")
            author_id = input(f"Enter an author id from this list {author_ids} ")
        selected_author = Author.find_by_id(author_id)
        new_name = input("Enter a new name: ")
        selected_author.name = new_name
        selected_author.update()
        print(f"\nAuthor's new name is {selected_author.name}")
    else:
        print("\nThere are no authors to edit")

def edit_post():
    all_posts = [f"{post.id}: {post.content}" for post in Post.get_all()]
    if len(all_posts) > 0:
        post_id = input(f"Enter a post id from this list {all_posts}: ")
        while post_id not in [str(post.id) for post in Post.get_all()]:
            print("Post id is not in list")
            post_id = input(f"Enter a post id from this list {all_posts}")
        selected_post = Post.find_by_id(post_id)
        new_content = input("Enter new content: ")
        selected_post.content = new_content
        author_name = Author.find_by_id(selected_post.author_id)
        selected_post.update()
        print(f"\nUpdated {selected_post.title} by {author_name.name}: {new_content}")
    else:
        print("\nThere are no posts to edit")
        


#? Delete features
def delete_post():
    post_titles = [post.title for post in Post.get_all()]
    title = input(f"Enter the post's title from this list {post_titles}: ")
    post = Post.find_by_title(title)
    if post:
        post.delete()
        print(f"\nPost -{title}- has been deleted")
    else :
        print(f"\nPost -{title}- not found")

def delete_author():
    author_ids = [f"{object.id}: {object.name}" for object in Author.get_all()]
    if len(author_ids) > 0:
        author_id = input(f"To remove an author, select an author id from this list {author_ids}: ")
        while author_id not in [str(object.id) for object in Author.get_all()]:
            print("Author id is not in list")
            author_id = input(f"To remove an author, select an author id from this list {author_ids}: ")
        selected_author = Author.find_by_id(author_id)
        print(f"\nYou deleted {selected_author.name} and all their posts")
        author_posts = [post for post in Post.get_all()]
        for post in author_posts:
            if str(post.author_id) == author_id:
                post.delete()
            else:
                continue
        selected_author.delete()
    else:
        print("\nThere are no authors to delete")

