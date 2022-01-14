
class Space:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = self.getName()
        self.hasPiece = False

    def getName(self):
        name = chr(self.x + ord('a')) + str(self.y + 1)
        return name
