from fastapi import FastAPI
from book import Book, Roman, Manga, BD, Comics
from author import Author
from series import Series
from type import Type
from code import Code

app = FastAPI()


@app.get("/toto")
async def root():
    return "Hello World"


@app.get("/Poulpy")
async def poulpy():
    return "Bonjour Poulpy"


@app.get("/greetings/{text}")
async def read_greetings(text: str):
    if text.lower() == "bonjour":
        return {"message": "Bonjour utilisateur"}

    else:
        return {"message": "Utilisateur malpoli"}


@app.get("/justePrix")
async def juste_prix(number: int):
    prix = 35
    print("Devinez le juste prix, c'est un nombre entre 1 et 50")

    if number < prix:
        return "Le juste prix est plus haut"
    if number > prix:
        return "Le juste prix est plus bas"
    if number == prix:
        return "Félicitations !"


@app.get("/demoBook")
async def book():
    livre1 = Book("Stupeurs et tremblements",
                  250,
                  Author("Nothomb",
                         42,
                         Type("contemporain",
                              "moderne",
                              Code(
                                  901,
                                   "Littérature française",
                                  "N"
                              )
                            )
                         )
                  )
    livre2 = Book("L'anomalie", 300, Author("LeTellier", 55, Type("contemporain", "littérature blanche",
                                                                  Code(902, "Littérature française", "L"))))
    for livre in [livre1, livre2]:
        livre.numberOfPage += 10
    livre1.title = "Métaphysique des tubes"
    if livre.numberOfPage > 300:
        livre.title = "Toto"
    return [livre1, livre2]


@app.get("/demoAuthor")
async def author():
    auteur = Author("Amélie Nothomb", 55, "contemporain")
    return auteur


@app.get("/demoSeries")
async def series():
    serie = Series("One Piece", 102, Type("action", "aventure", Code(903, "Mangas", "O")))
    return serie


@app.get("/demoListe")
async def liste():
    liste1 = [
        Book("Les Misérables", 500, None),
        Book("Guerre et paix", 600, None),
        Book("Anéantir", 350, None),
        Book("Lolita", 400, "Vladimir Nabokov"),
        Book("Harry Potter", 200, "J.K. Rowling"),
    ]
    for eLivre in liste1:
        if eLivre.author is None:
            eLivre.author = "auteur inconnu"
    for eLivre in liste1:
        if eLivre.title is "Les Misérables":
            eLivre.author = "Victor Hugo"
    liste1.append(Book("Germinal", 350, "Emile Zola"))
    for eLivre in liste1:
        if eLivre.title is "Harry Potter":
            eLivre.numberOfPage += 20
    roman = Roman("Preface de Jean", "Harry", 200, "JK")
    roman1 = Roman("Preface de Pierre", "Le Rêve", 150, "Emile Zola")
    manga = Manga("Kana", "action", "Naruto", 255, "Kishimoto")
    bd = BD("aventure", "Tintin", 150, "Hergé")
    comics = Comics("Marvel", "action", "IronMan", 250, "Collectif")
    return liste1, roman, roman1, manga, bd, comics
