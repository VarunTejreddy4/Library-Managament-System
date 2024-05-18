import os
import sys

def clear_screen():
    # This command works on Windows
    if os.name == 'nt':
        os.system('cls')
    # This command works on macOS and Linux
    else:
        os.system('clear')

def get_password(prompt="Enter password: "):
    print(prompt, end='', flush=True)
    password = []
    if os.name == 'nt':  # For Windows
        import msvcrt
        while True:
            char = msvcrt.getch()
            if char in {b'\r', b'\n'}:
                print()
                break
            elif char == b'\x08':  # Backspace
                if password:
                    password.pop()
                    print('\b \b', end='', flush=True)
            else:
                password.append(char.decode('utf-8'))
                print('*', end='', flush=True)
    else:  # For Unix-based systems
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                char = sys.stdin.read(1)
                if char in {'\r', '\n'}:
                    print()
                    break
                elif char == '\x7f':  # Backspace
                    if password:
                        password.pop()
                        print('\b \b', end='', flush=True)
                else:
                    password.append(char)
                    print('*', end='', flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ''.join(password)

def studentlogin():
    login_details = {}
    
    def login_credentials(nam, passw):
        login_details[nam] = passw

    def check_password_strength(password):
        uppercase_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        lowercase_chars = set('abcdefghijklmnopqrstuvwxyz')
        digits = set('0123456789')
        special_chars = set('!@#$%^&*()-_=+{}[]|;:\'",.<>/?`~')

        min_length = 8
        has_uppercase = any(char in uppercase_chars for char in password)
        has_lowercase = any(char in lowercase_chars for char in password)
        has_digit = any(char in digits for char in password)
        has_special = any(char in special_chars for char in password)

        if len(password) < min_length:
            print("Password must be at least 8 characters long.")
            return False
        if not has_uppercase:
            print("Password must contain at least one uppercase letter.")
            return False
        if not has_lowercase:
            print("Password must contain at least one lowercase letter.")
            return False
        if not has_digit:
            print("Password must contain at least one digit.")
            return False
        if not has_special:
            print("Password must contain at least one special character.")
            return False
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
            password = get_password("Enter your password: ")
            if check_password_strength(password):
                clear_screen()  # Clear screen after entering the password
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
            
            if name not in login_details:
                print("User not found.")
                create_new = input("Do you want to create a new account? (yes/no): \n").lower()
                if create_new == "yes":
                    new_user()
                else:
                    print("Okay, goodbye!")
                    return
            
            password = get_password("Enter your password:\n")
            clear_screen()  # Clear screen after entering the password

            if login_details.get(name) == password:
                print("Login successful!")
                try:
                    from studentsfunctins import manage_library
                    manage_library()
                except ImportError:
                    print("Library management module not found.")
                break
            else:
                print("Incorrect username or password.")
                reset_password = input("Forgot password? (yes/no): ").lower()
                if reset_password == "yes":
                    reset_new_password(name)
                    break
                else:
                    create_new = input("Do you want to create a new account? (yes/no): ").lower()
                    if create_new == "yes":
                        new_user()
                    else:
                        print("Okay, goodbye!")
                        break

    def reset_new_password(name):
        new_password = get_password("Enter your new password: ")
        clear_screen()  # Clear screen after entering the new password
        login_details[name] = new_password
        print("Password reset successfully.")

    while True:
        print("1. New user")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_user()
        elif choice == 2:
            user_login()
        elif choice == 3:
            break
        else:
            print("Invalid option. Please choose again.")

studentlogin()