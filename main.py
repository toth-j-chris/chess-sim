
### TESTING ###REMOVE
from GameBoardModel import GameBoardModel
### END TESTING

from GameBoardView import GameBoardView
import curses

def main(stdscr):
    stdscr.clear()
    curses.curs_set(False)

    boardDimension = 8
    tileWidth = 7
    tileHeight = 3

    gameBoardView = GameBoardView(boardDimension, tileWidth, tileHeight, stdscr)
    gameBoardModel = GameBoardModel(boardDimension)
    
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
