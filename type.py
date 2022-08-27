from code import Code

class Type:
    genre : str
    secondGenre : str
    code: Code

    def __init__(self, genre, secondGenre, code):
        self.genre = genre
        self.secondGenre = secondGenre
        self.code = code