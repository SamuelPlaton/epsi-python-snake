class Snake():

    def __init__(self):

        self.direction = 'X'
        self.historic = [[10, 10]]
        self.velocity = 5
        self.lives = 3

    def handleRapidity(self):
        if 5 + self.size < 30:
            self.velocity = 5 + self.size
        else:
            self.velocity = 30

    def checkDeath(self, width, heigth):
        lastPosition = self.historic[-1] # Head position
        x = lastPosition[0]
        y = lastPosition[1]
        previousPositions = self.historic[0:len(self.historic)-1] # All positions excepted head
        print(previousPositions)
        if x < 0 or x > width or y < 0 or y > heigth or [x, y] in previousPositions:
            self.lives -= 1

    # Moving our snake
    def moveSnake(self):
        lastMove = self.historic[-1]  # Position of the head of the snake

        # Retrieve the x and y of the next move
        if self.direction == 'R':
            x = lastMove[0] + 10
            y = lastMove[1]
        elif self.direction == 'L':
            x = lastMove[0] - 10
            y = lastMove[1]
        elif self.direction == 'U':
            x = lastMove[0]
            y = lastMove[1] - 10
        elif self.direction == 'D':
            x = lastMove[0]
            y = lastMove[1] + 10
        else:
            x = 0
            y = 0

        return [x, y]