class Snake():

    def __init__(self):
        self.size = 1
        self.x = 10
        self.y = 10
        self.direction = 'X'
        self.historic = [[10, 10]]

    def handleRapidity(self):
        if 5 + self.size < 30:
            return 5 + self.size
        else:
            return 30