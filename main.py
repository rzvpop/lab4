from domanin.book import Book


def run():
    b1 = Book(1, "Tow Sawyer", "faina, ma", "Mark Twain")

    print(b1)

    b1.desc("chiar faina")
    b1.desc()

    print(Book())

run()