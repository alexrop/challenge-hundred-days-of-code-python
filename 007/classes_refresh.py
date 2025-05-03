class Book:
    def __init__(self, title, author, chapters):
        self.title = title
        self.author = author
        self.chapters = chapters  # a list of chapter titles

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

    def __len__(self):
        return len(self.chapters)  # number of chapters

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False

    def __getitem__(self, index):
        return self.chapters[index]

    def __setitem__(self, index, value):
        self.chapters[index] = value



if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", ["Chapter 1", "Chapter 2"])
    book2 = Book("1984", "George Orwell", ["Intro", "Main"])

    print(str(book1))       # __str__: '1984' by George Orwell
    print(repr(book1))      # __repr__: Book(title='1984', author='George Orwell')

    print(len(book1))       # __len__: 2

    print(book1 == book2)   # __eq__: True (same title & author)

    print(book1[0])         # __getitem__: 'Chapter 1'
    book1[1] = "New Chapter 2"  # __setitem__
    print(book1.chapters)   # ['Chapter 1', 'New Chapter 2']