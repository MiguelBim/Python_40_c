# CHALLENGE NUMBER 22
# TOPIC: Dic Struct
# Database Admin Program
# https://www.udemy.com/course/the-art-of-doing/learn/lecture/17060820#overview


def admin_database(username, user_password, database_users):

    print("\nHello {}! You are logged in!".format(username))
    reset_pwd = input("Would you like to change your password (yes/no): ").lower().strip()

    if reset_pwd == "yes":
        new_pwd = input("What would you like your new password to be: ")
        if len(new_pwd) >= 8:
            database_users[username] = new_pwd
            print("\n{} your password is {}".format(username, new_pwd))
        else:
            print("{} not the minimum of eight characters.".format(new_pwd))
            print("\n{} your password is {}".format(username, user_password))
    else:
        print("Ok, goodbye!")

    return


if __name__ == '__main__':

    print("Welcome to the Database Admin Program")

    database_users = {
        "Mike21": "Mike21",
        "Tio129": "Tio129",
        "Pane28": "Pane28",
        "Yoli20": "Yoli20"
    }

    username = input("\nEnter your username: ").strip()

    if username == "admin00":
        password = input("Enter your password: ").strip()
        if password == "admin00":
            print("\nHello {}! You are logged in!".format(username))
            print("\nHere is the current user database: ")
            for user, pwd in database_users.items():
                print("Username: {}\t\tPassword: {}".format(user, pwd))
        else:
            print("Incorrect password for admin account.")
    elif username in database_users.keys():
        password = input("Enter your password: ").strip()
        if password == database_users[username]:
            admin_database(username, password, database_users)
        else:
            print("Incorrect password, Try again")
    else:
        print("Username not in database, goodbye.")