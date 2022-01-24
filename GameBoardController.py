import curses

from GameBoardModel import GameBoardModel

class GameBoardController:
    def __init__(self):
        self.__gameBoardModel = GameBoardModel()

    def getSpace(self, row, col):
        return self.__gameBoardModel.getSpace(row, col)

    def movePiece(self, moveString):
        if not len(moveString) == 4:
            return False
        else:
            file1 = ord(moveString[0]) - ord('a')
            rank1 = int(moveString[1]) - 1
            file2 = ord(moveString[2]) - ord('a')
            rank2 = int(moveString[3]) - 1
            self.__gameBoardModel.movePiece(file1, rank1, file2, rank2)
            return True

    def getBoardDimension(self):
        return self.__gameBoardModel.getBoardDimension()
