class Book():
    def __init__(self, title, author, price, width=10):
        self.title = title
        self.author = author
        self.price = price
        self.width = width

class Shelf():
    def __init__(self, width):
        self.shelf = []
        self.width = width

    def add_book(self, *books):
        for book in books:
            if self.width - self.get_current_width() >= book.width:
                self.shelf.append(book)
            else:
                raise NotEnoughWidth

    def get_current_width(self):
        return sum(book.width for book in self.shelf)
    def total_price(self):
        return sum(book.price for book in self.shelf)
    def __repr__(self):
        return '\n'.join(book.title for book in self.shelf)
    def has_book(self, book):
        for book in self.shelf:
            if book.title == book:
                return True
            else:
                return False

class NotEnoughWidth():
    pass

b1 = Book("A", "X", 30, 25)
b2 = Book("B", "Y", 30, 55)
b3 = Book("c", "z", 20, 30)
wood_shelf = Shelf(100)
wood_shelf.add_book(b1, b2)

print(wood_shelf)