from type import Type

class Author:
    name: str
    age: int
    type: Type

    def __init__(self, name, age, type):
        self.name = name
        self.age = age
        self.type = type
