class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            print("Price cannot be negative")
        else:
            self.__price = price

class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size


book = Book("Side Hustle", "Chris Guillebeau", 40)
print(book.title, book.get_price())

book.set_price(30)
print(book.get_price())

book.set_price(-4)

ebook = EBook("Side Hustle", "Chris Guillebeau", 40, 20.3)
print(ebook.title, ebook.get_price(), ebook.file_size)
        