from GameBoardController import GameBoardController

import curses

class GameBoardView:
    def __init__(self, tileWidth, tileHeight):
        self.__gameBoardController = GameBoardController()

        self.__boardDimension = self.__gameBoardController.getBoardDimension()
        self.__tileWidth = tileWidth
        self.__tileHeight = tileHeight

        curses.wrapper(self.__initWithCurses)

    def __initWithCurses(self, stdscr):
        
        self.__boardYOffset = int((curses.LINES / 2) - ((self.__boardDimension *
            self.__tileHeight) / 2))
        self.__boardXOffset = int((curses.COLS / 2) - ((self.__boardDimension *
            self.__tileWidth) / 2))

        self.__initColors()
        
        self.__stdscr = stdscr
        
        self.__stdscr.clear()
        curses.curs_set(False)
        curses.echo()

        self.__drawBoard()
        self.__drawPieces()
        self.__drawAxes()

        self.__inputLoop()

    def __initColors(self):
        whiteTileColor = curses.COLORS - 1
        blackTileColor = curses.COLORS - 2
        whitePieceColor = curses.COLORS - 3
        blackPieceColor = curses.COLORS - 4

        curses.init_color(whiteTileColor, 650, 650, 1000)
        curses.init_color(blackTileColor, 0, 0, 500)
        curses.init_pair(1, blackPieceColor, whiteTileColor)
        curses.init_pair(2, whitePieceColor, blackTileColor)
        self.__spaceColors = []
        self.__spaceColors.append(curses.color_pair(1))
        self.__spaceColors.append(curses.color_pair(2))

        curses.init_color(whitePieceColor, 900, 900, 900)
        curses.init_color(blackPieceColor, 0, 0, 0)
        curses.init_pair(3, whitePieceColor, whiteTileColor)
        curses.init_pair(4, blackPieceColor, blackTileColor)
        self.__pieceColors = []
        self.__pieceColors.append(curses.color_pair(3))
        self.__pieceColors.append(curses.color_pair(2))
        self.__pieceColors.append(curses.color_pair(1))
        self.__pieceColors.append(curses.color_pair(4))


    # Draw the board to stdscr 
    def __drawBoard(self):
        tileLine = " " * self.__tileWidth

        for file in range(self.__boardDimension):
            for rank in range(self.__boardDimension):
                currSpace = self.__gameBoardController.getSpace(file, rank)
                currColor = self.__spaceColors[currSpace.getColor()]
                currTileLocY = self.__boardYOffset + ((self.__boardDimension *
                        self.__tileHeight) - 1) - (self.__tileHeight * rank)
                currTileLocX = self.__boardXOffset + (self.__tileWidth * file)

                for k in range(self.__tileHeight):
                    self.__stdscr.addstr(currTileLocY - k, currTileLocX,
                            tileLine, currColor) 

    # Draw pieces on the board and refresh the screen
    def __drawPieces(self):
        tileCenterY = self.__boardYOffset + ((self.__boardDimension *
            self.__tileHeight) - 1) - int(self.__tileHeight / 2)
        tileCenterX = self.__boardXOffset + int(self.__tileWidth / 2)

        for file in range(self.__boardDimension):
            for rank in range(self.__boardDimension):
                currSpace = self.__gameBoardController.getSpace(file, rank)
                currSpaceColor = currSpace.getColor()
                currCenterY = tileCenterY - (self.__tileHeight * rank)
                currCenterX = tileCenterX + (self.__tileWidth * file)
                if currSpace.getCurrentPiece() is not None:
                    currPiece = currSpace.getCurrentPiece()
                    currPieceColor = currPiece.getColor()
                    currPieceSymbol = currPiece.getSymbol()
                    currColorCode = (currPieceColor * 2) + currSpaceColor
                    currColor = self.__pieceColors[currColorCode]
                    self.__stdscr.addstr(currCenterY, currCenterX,
                            currPieceSymbol, currColor | curses.A_BOLD)
                else:
                    self.__stdscr.addstr(currCenterY, currCenterX, " ",
                            self.__spaceColors[currSpaceColor])

        self.__stdscr.refresh()

    def __drawAxes(self):
        for i in range(self.__boardDimension):
            yAxisOffsetY = self.__boardYOffset + int(self.__tileHeight / 2) + (self.__tileHeight * i)
            yAxisOffsetX = self.__boardXOffset - 3
            xAxisOffsetY = self.__boardYOffset + (self.__boardDimension *
                    self.__tileHeight) + 1
            xAxisOffsetX = self.__boardXOffset + int(self.__tileWidth / 2) + (self.__tileWidth * i)
            self.__stdscr.addstr(yAxisOffsetY, yAxisOffsetX,
                    str(self.__boardDimension - i))
            self.__stdscr.addstr(xAxisOffsetY, xAxisOffsetX, chr(ord('a') + i))

    def __inputLoop(self):
        inputPrompt = "Input: "
        inputPositionY = self.__boardYOffset + (self.__boardDimension *
                self.__tileHeight) + 3
        inputPositionX = self.__boardXOffset + len(inputPrompt)
        userInput = ""
        inputString = ""
        while (not inputString == "quit"):
            inputString = ""
            self.__stdscr.addstr(inputPositionY, 0, " " * curses.COLS)
            self.__stdscr.move(inputPositionY, inputPositionX)
            self.__stdscr.addstr(inputPositionY, self.__boardXOffset,
                    inputPrompt) 
            while (True):
                userInput = self.__stdscr.getkey()
                if userInput == "\n":
                    break
                elif userInput == "KEY_BACKSPACE":
                    self.__stdscr.addstr(inputPositionY, inputPositionX +
                            len(inputString) - 1, " ")
                    inputString = inputString[0:len(inputString) - 1] 
                    self.__stdscr.move(inputPositionY, inputPositionX +
                            len(inputString))
                else:
                    inputString += userInput
            if not inputString == "quit":
                if self.__gameBoardController.movePiece(inputString):
                    self.__stdscr.addstr(inputPositionY + 1, 0, " " * curses.COLS)
                    self.__drawPieces()
                else:
                    self.__drawInputError()

    def __drawInputError(self):
        errorPositionY = self.__boardYOffset + (self.__boardDimension *
                self.__tileHeight) + 4
        errorPositionX = self.__boardXOffset
        self.__stdscr.addstr(errorPositionY, errorPositionX, "Invalid input, please try again.")
