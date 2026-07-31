# Library Management System using OOP

# ------------------ Book Class ------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)


# ------------------ Patron Class ------------------
class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}")
        print(f"Name: {self.name}")

        if self.borrowed_books:
            print("Borrowed Books:", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books: None")

        print("-" * 30)


# ------------------ Library Class ------------------
class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add Book
    def add_book(self, book):
        self.books[book.book_id] = book
        print("Book added successfully!")

    # Register Patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print("Patron registered successfully!")

    # Borrow Book
    def borrow_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}'.")

    # Return Book
    def return_book(self, patron_id, book_id):

        if patron_id not in self.patrons or book_id not in self.books:
            print("Invalid Patron ID or Book ID.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            patron.borrowed_books.remove(book.title)
            book.is_borrowed = False
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print("This patron did not borrow this book.")

    # Display Books
    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("\n------ Books ------")
            for book in self.books.values():
                book.display()

    # Display Patrons
    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
        else:
            print("\n------ Patrons ------")
            for patron in self.patrons.values():
                patron.display()


# ------------------ Main Program ------------------

library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == "3":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.borrow_book(patron_id, book_id)

    elif choice == "4":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.return_book(patron_id, book_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
        
