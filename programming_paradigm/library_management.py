class Book:
    def __init__(self, title, author):
        """Initialize a new book with a title, author, and its checked-out status"""
        self.title = title
        self.author = author
        self._is_checked_out = False  # The book starts as available (not checked out)

    def is_checked_out(self):
        """Check if the book is currently checked out"""
        return self._is_checked_out

    def check_out(self):
        """Mark the book as checked out, if it's available"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Already checked out

    def return_book(self):
        """Return the book to the library, making it available again"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # The book wasn't checked out
class Library:
    def __init__(self):
        """Initialize the library with an empty list of books"""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection"""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title, if available"""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out successfully.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title"""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned successfully.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are currently available for borrowing"""
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
