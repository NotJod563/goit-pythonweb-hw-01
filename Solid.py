from __future__ import annotations


import logging
from abc import ABC, abstractmethod
from typing import Callable, Dict, Iterable, List, Sequence


class Book:
    def __init__(self, t: str, a: str, y: int) -> None:
        self.title: str = t
        self.author: str = a
        self.year: int = y


class BookAdder(ABC):
    @abstractmethod
    def add_book(self, b: Book) -> None: ...


class BookRemover(ABC):
    @abstractmethod
    def remove_book(self, t: str) -> bool: ...


class BookLister(ABC):
    @abstractmethod
    def list_books(self) -> Iterable[Book]: ...


class LibraryInterface(BookAdder, BookRemover, BookLister):
    pass


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, b: Book) -> None:
        self.books.append(b)

    def remove_book(self, t: str) -> bool:
        for bk in list(self.books):
            if bk.title == t:
                self.books.remove(bk)
                return True
        return False

    def list_books(self) -> Iterable[Book]:
        return list(self.books)


class SortedLibrary(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, b: Book) -> None:
        self.books.append(b)

    def remove_book(self, t: str) -> bool:
        for bk in list(self.books):
            if bk.title == t:
                self.books.remove(bk)
                return True
        return False

    def list_books(self) -> Iterable[Book]:
        return sorted(self.books, key=lambda x: x.title)


class ReadonlyLibrary(BookLister):
    # приклад для перевірки ISP
    def __init__(self, books: Sequence[Book]) -> None:
        self.books: Sequence[Book] = books

    def list_books(self) -> Iterable[Book]:
        return list(self.books)


class LibraryManager:
    def __init__(self, lib: LibraryInterface) -> None:
        self.library: LibraryInterface = lib

    def add_book(self, t: str, a: str, y_str: str) -> None:
        try:
            y: int = int(y_str)
        except ValueError:
            logging.info("Рік має бути числом. Отримано: %s", y_str)
            return
        self.library.add_book(Book(t, a, y))
        logging.info("Додано: '%s' (%s, %d)", t, a, y)

    def remove_book(self, t: str) -> None:
        if self.library.remove_book(t):
            logging.info("Видалено: %s", t)
        else:
            logging.info("Не знайдено: %s", t)

    def show_books(self) -> None:
        bks = list(self.library.list_books())
        if not bks:
            logging.info("Бібліотека порожня")
            return
        for bk in bks:
            logging.info(
                "Title: %s, Author: %s, Year: %d", bk.title, bk.author, bk.year
            )


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    lib: LibraryInterface = SortedLibrary()
    man = LibraryManager(lib)

    def add_h() -> None:
        t = input("Enter book title: ").strip()
        a = input("Enter book author: ").strip()
        y = input("Enter book year: ").strip()
        man.add_book(t, a, y)

    def rem_h() -> None:
        t = input("Enter book title to remove: ").strip()
        man.remove_book(t)

    def show_h() -> None:
        man.show_books()

    cmds: Dict[str, Callable[[], None]] = {
        "add": add_h,
        "remove": rem_h,
        "show": show_h,
    }

    while True:
        cmd = input("Enter command (add, remove, show, exit): ").strip().lower()
        if cmd == "exit":
            break
        action = cmds.get(cmd)
        if action:
            action()
        else:
            logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
