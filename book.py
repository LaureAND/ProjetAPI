from author import Author


class Book:
    title: str
    numberOfPage: int
    author: Author

    def __init__(self, title, numberOfPage, author):
        self.title = title
        self.numberOfPage = numberOfPage
        self.author = author


class Roman(Book):
    preface: str

    def __init__(self, preface, title, numberOfPage, author):
        self.preface = preface
        Book.__init__(self, title, numberOfPage, author)


class BD(Book):
    genre: str

    def __init__(self, genre, title, numberOfPage, author):
        self.genre = genre
        Book.__init__(self, title, numberOfPage, author)


class Manga(BD):
    editor: str

    def __init__(self, editor, genre, title, numberOfPage, author):
        self.editor = editor
        BD.__init__(self, genre, title, numberOfPage, author)


class Comics(BD):
    licence: str

    def __init__(self,licence, genre,title, numberOfPage, author):
        self.licence = licence
        BD.__init__(self, genre, title, numberOfPage, author)
