import random
import string


def create_password(pass_length):
    if pass_length < 2 or pass_length > 18:
        print("Password should be in range between 0 to 15 entered by you!")
        exit()
    else:
        a = string.ascii_letters
        b = string.digits
        c = string.punctuation
        letters = a + b + c
    password = ''.join(random.choice(letters)
    for x in range(pass_length))
    return password
def register(users):

    username = input("Enter a username:\t")
    print("Do you want to generate password or are you want to set your own password:")

    passworduser_choice = input("generate or set:\t")
    if passworduser_choice.lower() == "generate":
        password_length = int(input("Enter the desired password length(2-18): "))
        password = create_password(password_length)
        print("Generated Password:\t", password)
    elif passworduser_choice.lower() == "set":
        password = input("Enter your password: ")
    else:
        print("Invalid choice. Try again.")
        return
    users[username] = password
    print("Congratulations! Registered Successfully")
def login(users):

    username = input("Enter your username: ")

    for password_attempts in range(0,3):

        password = input("Enter your password: ")

        if username in users and password == users[username]:
            print(f"Welcome, {username}!")
            return True

        print("Invalid username or password. Please try again.")
        password_attempts =password_attempts +1

    print("Exceeded maximum number of login attempts. Exiting.")
    return False
def uni():

    users = {}
    for i in range (1,4):
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        select= input("choose between following (1-3):\t")

        if select == "1":
            register(users)
        elif select== "2":
            if login(users):
                break
        elif select == "3":
            break
        else:
            print("TRY AGAIN")


if __name__ == "__main__":
    uni()
