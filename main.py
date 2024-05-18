from art import *
def display_menu():
    tprint('''Library  
Managament 
System''', font="cybermedium")
    print("1. Student Login")
    print("2. Teacher Login")
    print("3. Exit")
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        from studentlogin import studentlogin
        studentlogin()
    elif choice == '2':
        pass
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")