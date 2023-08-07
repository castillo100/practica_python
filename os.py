import os


def new_user():

    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to add: ")
        print("Add the username '" + username + "'?(Y/N)")
        confirm = input().upper()

    os.system("sudo useradd " + username)


def remove_user():

    confirm = "N"
    while confirm != "Y":
        username = input("Enter the name of the user to remove: ")
        print("Remove the username '" + username + "'?(Y/N)")
        confirm = input().upper()

    os.system("sudo userdel -r " + username)


new_user()
remove_user()
