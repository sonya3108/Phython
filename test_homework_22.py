import pytest



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




@pytest.fixture(scope="class")
def library():
    """Фікстура для створення бібліотеки на рівні класу."""
    return Library()

@pytest.fixture(scope="class")
def book1():
    """Фікстура для створення книги '1984'."""
    return Book("1984", "George Orwell")

@pytest.fixture(scope="class")
def book2():
    """Фікстура для створення книги 'To Kill a Mockingbird'."""
    return Book("To Kill a Mockingbird", "Harper Lee")


class TestLibrary:
    def test_add_book(self, library, book1, book2):
        library.add_book(book1)
        library.add_book(book2)
        assert len(library.books) == 2

    def test_remove_book(self, library, book1):
        library.remove_book(book1)
        assert len(library.books) == 1

    def test_list_books(self, library):
        books_list = library.list_books()
        assert books_list == ["'To Kill a Mockingbird' by Harper Lee"]



