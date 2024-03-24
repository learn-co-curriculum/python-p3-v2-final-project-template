from cli.pages import define_page

user_account_page = define_page("user_account", "User Account")
# Add options for user account page
user_account_page.add_option("Option 1", lambda: print("User Account - Option 1"))
user_account_page.add_option("Option 2", lambda: print("User Account - Option 2"))
# ... (Add more options as needed)