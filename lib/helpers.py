# lib/helpers.py
from models.author import Author 
from models.post import Post



#def helper_1():
#    print("Performing useful function#1.")


#? Adding features
def exit_program():
    print("Goodbye!")
    exit()

def add_author():
    author = input("Author name: ")
    Author.create(author)

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
        print("No authors found. Must add an author first.")
        create_menu()

    category = input(f"Enter a category from list of categories {Post.categories}: ")
    while category not in Post.categories:
        print("invalid category")
        category = input(f"Enter a category from list of categories {Post.categories}: ")
    content = input("Post content: ")
    Post.create(title, content, category, author_id)
    print("Post created successfully!")
    

    
#? Viewing features
def view_authors():
    authors = Author.get_all()
    if authors:
        for author in authors:
            print(f"\n{author.name} id:{author.id}")
    else :
        print("\nNo authors found\n")

def find_number_of_posts_by_author():
    authors = [f"{author.id}: {author.name}" for author in Author.get_all()]
    id_ = input(f"Input author's id to see number of posts. {authors}: ")
    try:
        author = Author.find_by_id(id_)
        authors_posts = author.find_all_posts()
        print(f"\nAuthor {author.name} has {len(authors_posts)} posts.\n")
    except Exception as exc:
        print(f"\nAuthor not found. {exc}\n")
        find_number_of_posts_by_author()
            

def find_author_by_id():
    id_ = input("Enter the author's id: ")
    author = Author.find_by_id(id_)
    if author:
        print(f"\nAuthor found: --{author.name}--\n") if author else print(f'\nAuthor {id_} not found\n')
    else: 
        print(f"\nAuthor {id_} not found\n")
        find_author_by_id()

def find_author_by_name():
    name = input("Enter the author's name: ")
    author = Author.find_by_name(name)
    print(f"\nAuthor found: --{author.name}--\n") if author else print(
        f'\nAuthor {name} not found\n')

#bug when author is deleted
def view_authors_posts():
    author_name = input("Enter the author's name: ")
    author_object = Author.find_by_name(author_name)
    if author_object:
        try:
            posts = author_object.find_all_posts()
            for post in posts:
                print(f"\nTitle: {post.title}, Category: {post.category} || {post.content}\n")
        except Exception as exc:
            print("Error finding posts: ", exc)
    else :
        print(f"\nAuthor named {author_name} not found\n")
        view_authors_posts()

#bug when author is deleted
def view_all_posts():
    posts = Post.get_all()
    if posts:
        for post in posts:
            author = Author.find_by_id(post.author_id)
            print(f"\nTitle: {post.title}, Category: {post.category}, Author: {author.name}|| {post.content}\n")
    else :
        print("\nNo posts found\n")

def view_posts_by_category():
    category = input("Enter the category: ")
    posts = Post.find_by_category(category)
    if posts:
        for post in posts:
            author = Author.find_by_id(post.author_id)
            print(f"\nTitle: {post.title}, Author: {author.name}|| {post.content}\n")
    else :
        print(f"\n{category} is not a valid category\n")
        view_posts_by_category()


#? Edit features
def edit_author():
    from cli import edit_menu
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
        print(f"Author's new name is {selected_author.name}")
    else:
        print("There are no authors to edit")
        edit_menu()

def edit_post():
    from cli import edit_menu
    all_posts = [f"{post.id}: {post.content}" for post in Post.get_all()]
    if len(all_posts) > 0:
        post_id = input(f"Enter a post id from this list {all_posts}: ")
        while post_id not in [str(post.id) for post in Post.get_all()]:
            print("Post id is not in list")
            post_id = input(f"Enter a post id from this list {all_posts}")
        selected_post = Post.find_by_id(post_id)
        new_content = input("Enter new content: ")
        selected_post.content = new_content
        selected_post.update()
        print(f"New post: {new_content}")

    else:
        print("There are no posts to edit")
        edit_menu


#? Delete features
def delete_post():
    post_titles = [post.title for post in Post.get_all()]
    title = input(f"Enter the post's title from this list {post_titles}: ")
    post = Post.find_by_title(title)
    if post:
        post.delete()
        print(f"\nPost -{title}- has been deleted\n")
    else :
        print(f"\nPost -{title}- not found\n")

def delete_author():
    from cli import delete_menu
    author_ids = [f"{object.id}: {object.name}" for object in Author.get_all()]
    if len(author_ids) > 0:
        author_id = input(f"To remove an author, select an author id from this list {author_ids} ")
        while author_id not in [str(object.id) for object in Author.get_all()]:
            print("Author id is not in list")
            author_id = input(f"To remove an author, select an author id from this list {author_ids} ")
        selected_author = Author.find_by_id(author_id)
        print(f"You deleted {selected_author.name} and all their posts")
        author_posts = [post for post in Post.get_all()]
        for post in author_posts:
            if str(post.author_id) == author_id:
                post.delete()
            else:
                continue
        selected_author.delete()
        
    else:
        print("There are no authors to delete")
        delete_menu()
