
def create_user_name(user_names):
    with open('./users.txt', 'a') as un:
        for user in user_names:
            
            un.write(user + '\n')

if __name__ == '__main__':
    user_names = []

    user = input("unsername, password: ")
    print("Username Created")
        
        

    create_user_name(user_names)