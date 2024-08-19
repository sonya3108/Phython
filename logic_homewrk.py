class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Додає книгу до бібліотеки."""
        self.books.append(book)
        print(f"{book} added to the library.")

    def remove_book(self, book):
        """Видаляє книгу з бібліотеки."""
        if book in self.books:
            self.books.remove(book)
            print(f"{book} removed from the library.")
        else:
            print(f"{book} is not in the library.")

    def list_books(self):
        """Повертає список книг у бібліотеці."""
        return [str(book) for book in self.books]




def main():
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")


    library = Library()


    library.add_book(book1)
    library.add_book(book2)


    print(library.list_books())  # ['1984 by George Orwell', 'To Kill a Mockingbird by Harper Lee']


    library.remove_book(book1)


    print(library.list_books())  # ['To Kill a Mockingbird by Harper Lee']




