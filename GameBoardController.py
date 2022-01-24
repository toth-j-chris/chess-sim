import curses

from GameBoardModel import GameBoardModel

class GameBoardController:
    def __init__(self):
        self.__gameBoardModel = GameBoardModel()

    def getSpace(self, row, col):
        return self.__gameBoardModel.getSpace(row, col)

    def movePiece(self, moveString):
        try:
            file1 = ord(moveString[0]) - ord('a')
            rank1 = int(moveString[1]) - 1
            file2 = ord(moveString[2]) - ord('a')
            rank2 = int(moveString[3]) - 1
            self.__gameBoardModel.movePiece(file1, rank1, file2, rank2)
            return True
        except (ValueError, IndexError):
            return False

    def __validMove(self, moveString):
        fileRange = range(ord('a'), ord('g'))
        rankRange = range(1, 9)
        if (ord(moveString[0]) in fileRange) and (int(moveString[1]) in rankRange) and (ord(moveString[2]) in fileRange) and (int(moveString[3]) in rankRange):
            return True
        else:
            return False

    def getBoardDimension(self):
        return self.__gameBoardModel.getBoardDimension()
