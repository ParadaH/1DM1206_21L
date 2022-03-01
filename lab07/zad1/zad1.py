from book import Book

if __name__ == "__main__":

    book_1 = Book("Podroz do wnetrza ziemii", "Julius Verne", 1989, 2, "soft")
    book_2 = Book("Romeo i Julia", "Wiliam Shakespear", 1784, 1, "hard")
    book_3 = Book("Krotka historia czasu", "Stephen Hawking", 1995, 1, "soft")
    book_4 = Book("Krotkie odpowiedzi na wielkie pytania", "Stephen Hawking", 2001, 4, "hard")
    book_5 = Book("Krotkie odpowiedzi na wielkie pytania", "Stephen Hawking", 2000, 1, "soft")
    book_6 = Book("Sherlock Holmes", "Arthur Conan Doyle", 1809, 12, "hard")

    collection = {book_1, book_2, book_3, book_4}
    unique_set_of_books = set(collection)

    print("Collection of unique books:")
    for book in unique_set_of_books:
        print(book)
