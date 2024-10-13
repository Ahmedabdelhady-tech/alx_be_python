# Base class for books
class Book:
    def __init__(self, title, author):
        """Initialize a book with a title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a book."""
        return f"Book: {self.title} by {self.author}"


# Derived class for EBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with file size."""
        super().__init__(title, author)  # Initialize title and author from the base class
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class for Print Books
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with page count."""
        super().__init__(title, author)  # Initialize title and author from the base class
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition: Library class that manages a collection of books
class Library:
    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
