# Iterating the objects in a class 

class BookCollection:
    def __init__(self):
        self.books = ['Harry Potter', 'Ring', 'Game of Thrones']
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.books):
            raise StopIteration()
        r = self.books[self.count]
        self.count += 1
        return r

books = BookCollection()
for book in books:
    print(book)