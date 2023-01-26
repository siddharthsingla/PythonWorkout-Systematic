PASSWORD = {}
def username_password():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if username not in PASSWORD:
        print("Invalid username")
    elif PASSWORD[username] != password:
        print("Invalid password")
    else:
        print("WELCOME")
