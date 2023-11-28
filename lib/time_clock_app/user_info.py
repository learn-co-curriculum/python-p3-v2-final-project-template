# this function will carry all of the classes that are user info related

class User:
# this class will hold the username and password
    all= []

    def __init__(self, username, password):
        self._username = username
        self._password = password
        type(self).all.append(self) # adds all of the .self to the ass array/list

    @property
    def username(self):
        return self._username
    @username.setter
    def username (self,value):
        if isinstance(value,Username):
            self._username = value
            return self._username
        
class Username:

    all = []

    def __init__(self,username):
        self._username = username
        type(self).all.append(self)

# get/set username
    @property
    def username(self):
        return self._username
    @username.setter
    def username (self,value):
        if isinstance(value,str) and 1<= len(value) <= 10:
            self._username = value
            return self._username

class Password:

    all = []

    def __init__(self,password):
        self._password = password
        