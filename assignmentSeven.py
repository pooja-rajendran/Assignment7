#LOGGING DECORATOR

def login_required(fun):
    def wrapper(user):
        if user == "quest":
            fun()
        else:
            print("Access denied. Please login first.")
    return wrapper


def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "quest" and password == "quest123":
        print("Login successful")
        return username
    else:
        print("Invalid username or password")
        return "guest"


def home():
    print("Welcome to Home")


@login_required
def about():
    print("Welcome to About")


@login_required
def profile():
    print("Welcome to Profile")


user = "guest"

while True:

    print("\n--- MENU ---")
    print("1. Home")
    print("2. About")
    print("3. Profile")
    print("4. Login")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        home()

    elif choice == "2":
        about(user)

    elif choice == "3":
        profile(user)

    elif choice == "4":
        user = login()

    elif choice == "5":
        print("Thank you")
        break

    else:
        print("Invalid choice")