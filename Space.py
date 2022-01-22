from Piece import Piece

class Space:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__name = ""
        self.__setName()
        self.__currentPiece = None

    def __setName(self):
        self.__name = chr(self.__x + ord('a')) + str(self.__y + 1)

    def getCurrentPiece(self):
            return self.__currentPiece

    def setCurrentPiece(self, piece):
        self.__currentPiece = piece
