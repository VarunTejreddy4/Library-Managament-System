def manage_teacher_library():
    def display_menu2():
        print("1. Add book")
        print("2. Remove book")
        print("3. Display available books")
        print("4. Add book taken by student")
        print("5. Remove book taken by student")
        print("6. Display books taken by student")
        print("7. Exit")

    def add_books_library(library):
        print("Enter book details:")
        bookname = input("Enter book name: ")
        authorname = input("Enter author name: ")
        quantity = int(input("Enter quantity: "))
        book_exists = False
        for book_id, book_info in library.items():
            if book_info["book_name"] == bookname and book_info["author_name"] == authorname:
                library[book_id]["quantity"] += quantity
                print("Book quantity updated successfully!")
                book_exists = True
                break
        if not book_exists:
            new_book_id = len(library) + 1
            library[new_book_id] = {"book_name": bookname, "author_name": authorname, "quantity": quantity}
            print("Book added to the library successfully!")

    def remove_books_library(library):
        print("Enter book details to remove:")
        bookname = input("Enter book name: ")
        authorname = input("Enter author name: ")
        book_found = False
        for book_id, book_info in library.items():
            if book_info["book_name"] == bookname and book_info["author_name"] == authorname:
                book_found = True
                del library[book_id]
                print("Book removed from the library successfully!")
                break
        if not book_found:
            print("Book not found in the library.")

    def display_available_books(library):
        if library:
            print("Available books in the library:")
            for book_id, book_info in library.items():
                print(f"ID: {book_id}, Title: {book_info['book_name']}, Author: {book_info['author_name']}, Quantity: {book_info['quantity']}")
        else:
            print("No books available in the library.")

    def add_book_taken_by_student(library, student_books):
        student_id = input("Enter student ID: ")
        bookname = input("Enter book name: ")
        authorname = input("Enter author name: ")

        # Check if the book exists in the library
        book_found = False
        for book_id, book_info in library.items():
            if book_info["book_name"] == bookname and book_info["author_name"] == authorname:
                book_found = True
                if library[book_id]["quantity"] > 0:
                    library[book_id]["quantity"] -= 1
                    if student_id not in student_books:
                        student_books[student_id] = []
                    student_books[student_id].append({"book_name": bookname, "author_name": authorname})
                    print("Book added to student's account successfully!")
                else:
                    print("Sorry, this book is out of stock.")
                break

        if not book_found:
            print("Book with the specified details not found in the library.")
    def remove_book_taken_by_student(library, student_books):
        student_id = input("Enter student ID: ")
        bookname = input("Enter book name: ")
        authorname = input("Enter author name: ")
        book_found = False
        if student_id in student_books:
            for book in student_books[student_id]:
                if book["book_name"] == bookname and book["author_name"] == authorname:
                    book_found = True
                    student_books[student_id].remove(book)
                    for book_id, book_info in library.items():
                        if book_info["book_name"] == bookname and book_info["author_name"] == authorname:
                            library[book_id]["quantity"] += 1
                            break
                    print("Book removed from student's account successfully!")
                    break
        if not book_found:
            print("The student does not have the specified book.")
    student_books={}
    while True:
        display_menu2()
        choice = input("Enter your choice: ")
        if choice == '1':
            from bookslist import library
            add_books_library(library)
        elif choice == '2':
            from bookslist import library
            remove_books_library(library)
        elif choice == '3':
            from bookslist import library
            print("Book ID\tBook Name\t\t\tAuthor Name\t\tQuantity")
            print("-------------------------------------------------------------")
            for book_id, book_info in library.items():
                print(f"{book_id}\t{book_info['book_name']: <30}\t{book_info['author_name']: <20}\t{book_info['quantity']}")
        elif choice == '4':
            from bookslist import library
            add_book_taken_by_student(library,student_books)
        elif choice == '5':
            from bookslist import library
            remove_book_taken_by_student(library, student_books)
        elif choice == '6':
            student_id = input("Enter student ID: ")
            if student_id in student_books:
                print(f"Books taken by student ID {student_id}:")
                for book in student_books[student_id]:
                    print(f"{book['book_name']} - {book['author_name']}")
            else:
                print("No books found for this student ID.")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
manage_teacher_library()


