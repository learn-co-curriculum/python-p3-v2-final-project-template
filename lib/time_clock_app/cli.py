#user class
# can't figure out how I used ipdb in the code challenge XD gotta do tat ad make this functional to set pinput values to an array or value in the usernames and passwords....
import ipdb
class User:
    all = []

    def __init__(self, pass_word, user_name):
        self._password = pass_word
        self._username = user_name
        type(self).all.append(self)
# props for user
    @property
    def password(self):
        return self._password
# setters for user

# cli info setting to txt file
def create_user_name(user_names):
    with open('./time_clock_app/users.txt', 'a') as un:
        for user in user_names:
            un.write(user + '\n')
# cli for project
if __name__ == '__main__':
    user_names = []

    user = input("unsername, password: ")
    while user:
        user_names.append(user)
        user = input("username, password: ")

    create_user_name(user_names)