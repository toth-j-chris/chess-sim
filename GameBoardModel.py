
from Space import Space

# [
# i[j, j, j, j],
# i[j, j, j, j],
# i[j, j, j, j],
# i[j, j, j, j]
# ]

class GameBoardModel:
    def __init__(self, boardDimension):
        self.boardDimension = boardDimension
        self.initSpaces()

    def initSpaces(self):
        self.spaces = []

        for i in range(self.boardDimension - 1, -1, -1):
            self.spaces.append([])
            for j in range(self.boardDimension):
                self.spaces[((self.boardDimension - 1) - i)].append(Space(j, i))
