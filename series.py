from type import Type

class Series:
    name: str
    numberOfVolume: int
    type: Type

    def __init__(self, name, numberOfVolume, type):
        self.name = name
        self.numberOfVolume = numberOfVolume
        self.type = type