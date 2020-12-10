class Snake():

    def __init__(self, interface_heigth):
        self.size = 1
        self.direction = 'X'
        self.historic = [[10, 10+interface_heigth]]
        self.velocity = 5
        self.lives = 3

    def handleRapidity(self):
        if 5 + self.size < 30:
            self.velocity = 5 + self.size
        else:
            self.velocity = 30

    def checkDeath(self, width, heigth, interface_heigth, obstacles):
        lastPosition = self.historic[-1] # Head position
        x = lastPosition[0]
        y = lastPosition[1]
        previousPositions = self.historic[0:len(self.historic)-1] # All positions excepted head
        # If snake is out of range or touches himself, he dies
        if x < 0 or x >= width or y < interface_heigth or y >= heigth or [x, y] in previousPositions or [x, y] in obstacles:
            self.lives -= 1
            return True
        else:
            return False

    # Moving our snake
    def moveSnake(self, interface_heigth):
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
            x = 10
            y = interface_heigth+10
        return [x, y]

    # Respawn our snake
    def respawn(self, width, interface_heigth):
        historic = []
        direction = 'R'
        i = 0
        i2 = 0
        y = interface_heigth+10
        x = 10
        # Handle respawn to make the snake respawn in the top-left hand corner
        # Handle conditions to make him respawn completely in "zig-zag" form if he's too long for a single line
        while i < self.size:
            historic.append([x, y])
            if direction == 'R':
                x += 10
            else:
                x -=10
            if i2*10+10 > width:
                i2 = 0
                y += 10
                if direction == 'R':
                    x = width-10
                    direction == 'L'
                else:
                    x = 10
                    direction == 'R'
            i2 += 1
            i += 1
        self.direction = 'D'
        self.historic = historic
