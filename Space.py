from Piece import Piece

class Space:
    def __init__(self, file, rank, color):
        self.__file = file
        self.__rank = rank
        self.__color = color
        self.__name = ""
        self.__setName()
        self.__currentPiece = None

    def __setName(self):
        self.__name = chr(self.__file + ord('a')) + str(self.__rank + 1)

    def getCurrentPiece(self):
        return self.__currentPiece

    def setCurrentPiece(self, piece):
        self.__currentPiece = piece

    def getColor(self):
        return self.__color
