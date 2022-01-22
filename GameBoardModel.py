from Space import Space
from Piece import Piece

# [
# i[j, j, j, j],
# i[j, j, j, j],
# i[j, j, j, j],
# i[j, j, j, j]
# ]

class GameBoardModel:
    def __init__(self):
        self.__boardDimension = 8
        self.__spaces = []
        self.__pieces = []
        self.__initSpaces()
        self.__initPieces()

    def __initSpaces(self):
        for i in range(self.__boardDimension - 1, -1, -1):
            self.__spaces.append([])
            for j in range(self.__boardDimension):
                self.__spaces[((self.__boardDimension - 1) - i)].append(Space(j, i))

    def __initPieces(self):
        for i in range(len(self.__spaces)):
            if i > 5 or i < 2:
                for j in range(len(self.__spaces[i])):
                    self.__spaces[i][j].setCurrentPiece(Piece())

    def getSpace(self, row, col):
        return self.__spaces[row][col]
