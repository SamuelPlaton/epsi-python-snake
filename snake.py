class Snake():

    def __init__(self):
        self.size = 1
        self.direction = 'X'
        self.historic = [[10, 10]]
        self.velocity = 5

    def handleRapidity(self):
        if 5 + self.size < 30:
            self.velocity = 5 + self.size
        else:
            self.velocity = 30

    def checkDeath(self, width, heigth):
        if ...:
            return True
        else:
            return False