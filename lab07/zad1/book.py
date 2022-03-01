class Book:

    def __init__(self, title, author, release_date, edition, cover):
        self.__title = title
        self.__author = author
        self.__release_date = release_date
        self.__edition = edition
        self.__cover = cover

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def __hash__(self):
        return (self.__title, self.__author).__hash__()

    def __eq__(self, other):
        return  self.__class__ == other.__class__ \
            and self.__title == other.get_title() \
            and self.__author == other.get_author()

    def __repr__(self):
        cls = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"[{cls}: {attrs}]"