class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password  # In a real application, ensure this is hashed

    def register(self, db_connection):
        """
        Register a new user in the database.
        :param db_connection: Database connection object
        """
        try:
            cursor = db_connection.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", 
                           (self.username, self.password))
            db_connection.commit()
            print(f"User {self.username} registered successfully.")
        except Exception as e:
            print(f"Error registering user: {e}")

    def login(self, db_connection):
        """
        Authenticate a user.
        :param db_connection: Database connection object
        """
        try:
            cursor = db_connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", 
                           (self.username, self.password))
            user = cursor.fetchone()
            if user:
                print(f"User {self.username} logged in successfully.")
                return True
            else:
                print("Invalid username or password.")
                return False
        except Exception as e:
            print(f"Error logging in: {e}")
            return False

    def logout(self):
        """
        Log out the user.
        """
        print(f"User {self.username} logged out.")
