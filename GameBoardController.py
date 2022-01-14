
import curses

from GameBoardView import GameBoardView
from GameBoardModel import GameBoardModel

class GameBoardController:
    def __init__(self):
        curses.wrapper(self._init)
        
    def _init(self, stdscr):
        stdscr.clear()
        curses.curs_set(False)
        self.GameBoardView = GameBoardView(stdscr)
        self.GameBoardModel = GameBoardModel(self.GameBoardView.boardDimension)
        stdscr.refresh()
        stdscr.getkey()

