from GameBoardController import GameBoardController

import curses

class GameBoardView:
    def __init__(self):
        curses.wrapper(self._init)

    def _init(self, stdscr):
        self.gameBoardController = GameBoardController()
        self.boardDimension = 8
        self.tileWidth = 7 
        self.tileHeight = 3
        self.stdscr = stdscr
        
        self.stdscr.clear()
        curses.curs_set(False)

        self.drawBoard()

        stdscr.refresh()
        stdscr.getkey()

    # Draw the board to stdscr 
    def drawBoard(self):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
        whiteTileColor = curses.color_pair(1)
        blackTileColor = curses.color_pair(2)

        tileLine = " " * self.tileWidth
        colorSwitch = True

        heightCount = 0
        yOffset = 5
        xOffset = int((curses.COLS / 2) - ((self.boardDimension * self.tileWidth) /
                2))

        for i in range(yOffset, self.tileHeight * self.boardDimension + yOffset):
            heightCount += 1
            for j in range(xOffset, self.tileWidth * self.boardDimension +
                    xOffset, self.tileWidth):
                if colorSwitch:
                    self.stdscr.addstr(i, j, tileLine, whiteTileColor)
                    colorSwitch = False
                else:
                    self.stdscr.addstr(i, j, tileLine, blackTileColor)
                    colorSwitch = True
            if heightCount == self.tileHeight:
                if colorSwitch:
                    colorSwitch = False
                else:
                    colorSwitch = True
                heightCount = 0

