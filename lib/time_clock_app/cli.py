
def create_user_name(user_names):
    with open('./users.txt', 'a') as un:
        for user in user_names:
            # add '\n' to write grades on separate lines
            un.write(user + '\n')

if __name__ == '__main__':
    user_names = []

    user = input("unsername, password: ")
    while user:
        user_names.append(user)
        # end when no grade is entered
        user = input("username, password: ")

    create_user_name(user_names)