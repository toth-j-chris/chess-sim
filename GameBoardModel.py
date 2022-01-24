from Space import Space
from Piece import Piece

# Data representing the state of the board
class GameBoardModel:
    def __init__(self):
        self.__boardDimension = 8
        self.__spaces = []
        self.__pieces = []
        self.__initSpaces()
        self.__initPieces()

    # Initialize a matrix of spaces to represent the board
    def __initSpaces(self):
        color = 0
        for file in range(self.__boardDimension):
            color = self.__switchColor(color)
            self.__spaces.append([])

            for rank in range(self.__boardDimension):
                self.__spaces[file].append(Space(file, rank, color))
                color = self.__switchColor(color)

    def __switchColor(self, color):
        if color == 0:
            color = 1
        else:
            color = 0
        return color

    # Initialize pieces in their starting position
    def __initPieces(self):
        for file in range(self.__boardDimension):
            for rank in range(self.__boardDimension):
                if rank > 5:
                    self.__spaces[file][rank].setCurrentPiece(Piece(1))
                elif rank < 2:
                    self.__spaces[file][rank].setCurrentPiece(Piece(0))
        
    # Moves a piece from first pair of coordinates to the second
    def movePiece(self, file1, rank1, file2, rank2):
        space1 = self.__spaces[file1][rank1]
        space2 = self.__spaces[file2][rank2]
        
        space2.setCurrentPiece(space1.getCurrentPiece())
        space1.setCurrentPiece(None)

    # Returns boardDimension
    def getBoardDimension(self):
        return self.__boardDimension

    # Takes two coordinates and returns the corresponding space
    def getSpace(self, file, rank):
        return self.__spaces[file][rank]
