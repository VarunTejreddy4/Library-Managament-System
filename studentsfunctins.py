def manage_library():
    def display_menu():
        print("1. Add book")
        print("2. Remove book")
        print("3. Display your books")
        print("4. Display available book in library")
        print("5. Exit")
    def student_take_book(library, taken_books):
        print("Enter book details:")
        bookname = input("Enter book name: ")
        authorname = input("Enter author name: ")
        book_found = False
        for book_id, book_info in library.items():
            if book_info["book_name"] == bookname and \
            book_info["author_name"] == authorname:
                book_found = True
                break
        if book_found and library[book_id]["quantity"] > 0:
            library[book_id]["quantity"] -= 1
            if book_id not in taken_books:
                taken_books[book_id] = {"book_name": bookname, "author_name": authorname, "quantity": 1}
            else:
                taken_books[book_id]["quantity"] += 1 
            print("Book taken successfully!")
        elif book_found:
            print("Sorry, this book is out of stock.")
        else:
            print("Book with the specified details not found in the library.")
    def remove_book(library,taken_books):
        print("Enter book details to remove:")
        bookname = input("Enter book name: ")
        authorname = input("Enter author name: ")
        book_removed = False
        for book_id, book_info in taken_books.items():
            if book_info["book_name"] == bookname and book_info["author_name"] == authorname:
                del taken_books[book_id]
                print("Book removed successfully!")
                book_removed = True
                break
        else:
            print("Book with the specified details not found in the library.")
        if book_removed:
            library[book_id]["quantity"] += 1
        elif book_id not in taken_books:
            taken_books[book_id] = {"book_name": bookname, "author_name": authorname, "quantity": 1}
    taken_books = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            from bookslist import library
            student_take_book(library, taken_books)
        elif choice == '2':
            from bookslist import library
            remove_book(library,taken_books)
        elif choice == '3':
            print("Taken Books:")
            print("Book ID\tBook Name\t\t\tAuthor Name\t\tQuantity")
            print("-------------------------------------------------------------")
            for book_id, book_info in taken_books.items():
               print(f"{book_id}\t{book_info['book_name']: <30}\t{book_info['author_name']: <20}\t{book_info['quantity']}")
        elif choice == '4':
            from bookslist import library
            print("Book ID\tBook Name\t\t\tAuthor Name\t\tQuantity")
            print("-------------------------------------------------------------")
            for book_id, book_info in library.items():
               print(f"{book_id}\t{book_info['book_name']: <30}\t{book_info['author_name']: <20}\t{book_info['quantity']}")
        elif choice == '5':
            print("Thank you for using the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")
manage_library()