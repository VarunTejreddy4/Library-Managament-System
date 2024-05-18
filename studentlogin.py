import os
def studentlogin():
    def clear_screen():
        if os.name == 'nt':
            os.system('cls')
    login_details = {}
    def login_credentials(nam,passw):
        login_details[nam]=passw
    def check_password_strength(password):
        uppercase_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lowercase_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '`', '~']
        min_length = 8
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special = False
        for char in password:
            if char in uppercase_chars:
                has_uppercase = True
            elif char in lowercase_chars:
                has_lowercase = True
            elif char in digits:
                has_digit = True
            elif char in special_chars:
                has_special = True
        if len(password) < min_length:
            print("Password must be at least 8 characters long.")
            return False
        elif not has_uppercase:
            print("Password must contain at least one uppercase letter.")
            return False
        elif not has_lowercase:
            print("Password must contain at least one lowercase letter.")
            return False
        elif not has_digit:
            print("Password must contain at least one digit.")
            return False
        elif not has_special:
            print("Password must contain at least one special character.")
            return False
        else:
            return True 
    def new_user():
        print("Enter your Hall Ticket Number:")
        while True:
            name = input().upper()
            if not name.startswith("23P81A"):
                print("Username must start with '23P81A'. Please try again.")
            else:
                break
        if name in login_details:
            print("User already exists. Please login")
            return
        while True:
            print("Enter your password: ")
            password = input()
            if check_password_strength(password):
                clear_screen()
                print("Successfully created. Please login.")
                login_credentials(name, password)
                return
            else:
                print("Please choose a stronger password.")
    def user_login():
        while True:
            name = input("Enter your Hall Ticket Number:\n").upper()
            if not name.startswith("23P81A"):
                print("Username must start with '23P81A'. Please try again.")
                continue
            elif name not in login_details:
                print("User not found.")
                create_new = input("Do you want to create a new account? (yes/no): \n").lower()
                if create_new == "yes":
                    new_user()
                else:
                    print("Okay, goodbye!")
                    return
            attempts = 3
            while attempts > 0:
                password = input("Enter your password:\n")
                clear_screen()
                if login_details[name] == password:
                    print("Login successful!")
                    from studentsfunctins import manage_library
                    manage_library()
                    return
                else:
                    attempts -= 1
                    print(f"Incorrect password. You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
            if attempts == 0:
                reset_password = input("Forgot password? (yes/no): ").lower()
                if reset_password == "yes":
                    reset_new_password(name)
                    return
                else:
                    create_new = input("Do you want to create a new account? (yes/no): ").lower()
                    if create_new == "yes":
                        new_user()
                    else:
                        print("Okay, goodbye!")
                        return
    def reset_new_password(name):
        while True:
            new_password = input("Enter your new password: ")
            if check_password_strength(new_password):
                clear_screen()
                login_details[name] = new_password
                print("Password reset successfully.")
                return
    while True:
        print("1.New user")
        print("2.Login")
        print("3.Exit")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            new_user()
        elif choice == 2:
            user_login()
        elif choice == 3:
            break
        else:
            print("Invalid option. Please choose again.")
studentlogin()
