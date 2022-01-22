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
        self.boardYOffset = 5
        self.boardXOffset = int((curses.COLS / 2) - ((self.boardDimension *
            self.tileWidth) / 2))
        self.stdscr = stdscr
        
        self.stdscr.clear()
        curses.curs_set(False)

        self.drawBoard()
        self.drawPieces()

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

        for i in range(self.boardYOffset, self.tileHeight * self.boardDimension + self.boardYOffset):
            heightCount += 1
            for j in range(self.boardXOffset, self.tileWidth * self.boardDimension +
                    self.boardXOffset, self.tileWidth):
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

    def drawPieces(self):
        tileWidthOffset = int(self.tileWidth / 2)
        tileHeightOffset = int(self.tileHeight / 2)

        for i in range(self.boardDimension):
            for j in range(self.boardDimension):
                if self.gameBoardController.getSpace(i, j).getCurrentPiece() is not None:
                    self.stdscr.addstr(self.boardYOffset + tileHeightOffset + (self.tileHeight *
                        i), self.boardXOffset + tileWidthOffset + (self.tileWidth * j),
                        self.gameBoardController.getSpace(i,
                            j).getCurrentPiece().getSymbol(),
                        curses.color_pair(1))
