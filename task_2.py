from typing import List
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> List[Book]:
        pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        self._books = [book for book in self._books if book.title != title]

    def get_books(self) -> List[Book]:
        return self._books


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logger.info('Book "%s" added successfully.', title)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)
        logger.info('Book "%s" removed successfully.', title)

    def show_books(self) -> None:
        books: List[Book] = self.library.get_books()
        if books:
            logger.info("Books in the library:")
            for book in books:
                logger.info("%s", str(book))
        else:
            logger.info("The library is empty.")


class ExtendedLibrary(Library):
    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self._books if book.author == author]


def main() -> None:
    library = ExtendedLibrary()
    manager = LibraryManager(library)

    manager.add_book("The Forest Song", "Lesya Ukrainka", "1912")
    manager.add_book("Mina Mazailo", "Mykhailo Kotsiubynsky", "1910")
    manager.show_books()

    manager.remove_book("Mina Mazailo")
    manager.show_books()


if __name__ == "__main__":
    main()
