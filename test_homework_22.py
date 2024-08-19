import pytest

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




