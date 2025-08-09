from abc import ABC, abstractmethod

class Book:
    def __init__(self, t, a, y):
        self.title = t
        self.author = a
        self.year = y

class BookAdder(ABC):
    @abstractmethod
    def add_book(self, b):
        pass

class BookRemover(ABC):
    @abstractmethod
    def remove_book(self, t):
        pass

class BookLister(ABC):
    @abstractmethod
    def list_books(self):
        pass

class LibraryInterface(BookAdder, BookRemover, BookLister):
    pass

class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, b):
        self.books.append(b)

    def remove_book(self, t):
        for bk in self.books:
            if bk.title == t:
                self.books.remove(bk)
                return True
        return False

    def list_books(self):
        return list(self.books)

class SortedLibrary(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, b):
        self.books.append(b)

    def remove_book(self, t):
        for bk in self.books:
            if bk.title == t:
                self.books.remove(bk)
                return True
        return False

    def list_books(self):
        return sorted(self.books, key=lambda x: x.title)

class ReadonlyLibrary(BookLister):
    # приклад для перевірки ISP
    def __init__(self, books):
        self.books = books

    def list_books(self):
        return list(self.books)

class LibraryManager:
    def __init__(self, lib):
        self.library = lib

    def add_book(self, t, a, y):
        self.library.add_book(Book(t, a, y))

    def remove_book(self, t):
        if self.library.remove_book(t):
            print("Removed:", t)
        else:
            print("Not found:", t)

    def show_books(self):
        bks = self.library.list_books()
        if not bks:
            print("Library is empty")
        for bk in bks:
            print("Title:", bk.title, ", Author:", bk.author, ", Year:", bk.year)

def main():
    lib = SortedLibrary()
    man = LibraryManager(lib)

    def add_h():
        t = input("Enter book title: ").strip()
        a = input("Enter book author: ").strip()
        y = input("Enter book year: ").strip()
        man.add_book(t, a, y)

    def rem_h():
        t = input("Enter book title to remove: ").strip()
        man.remove_book(t)

    def show_h():
        man.show_books()

    cmds = {
        "add": add_h,
        "remove": rem_h,
        "show": show_h
    }

    while True:
        cmd = input("Enter command (add, remove, show, exit): ").strip().lower()
        if cmd == "exit":
            break
        if cmd in cmds:
            cmds[cmd]()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
