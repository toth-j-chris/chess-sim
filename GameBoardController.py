
import curses

from GameBoardModel import GameBoardModel

class GameBoardController:
    def __init__(self):
        self.gameBoardModel = GameBoardModel()

    def getSpace(self, row, col):
        return self.gameBoardModel.getSpace(row, col)
