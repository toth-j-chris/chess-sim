class Piece:
    def __init__(self, color):
        self.__name = "test"
        self.__symbol = "Q"
        self.__color = color

    def getSymbol(self):
        return self.__symbol

    def getColor(self):
        return self.__color
