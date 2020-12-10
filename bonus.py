import random
import time

class Bonus():
    def __init__(self):
        self.type = ''
        self.active = False
        self.duration = 30
        self.color = (0, 0, 0)

    def spawnBonus(self):
        r = random.randint(1, 10)
        if r == 1:
            self.active = True
            type = random.randint(1, 4)
            if type == 1:
                self.type = 'slow'
                self.color = (0, 0, 255)
            elif type == 2:
                self.type = 'fast'
                self.color = (255, 127, 0)

    def checkBonusEaten(self, x, y):
        # If yes, increment score, snake size, apples eaten and set a new random position for apple
        if x == self.current[0] and y == self.current[1]:

            self.bonuseaten += 1
            self.iseaten = True
            self.active = False
            return self.iseaten
        else:
            return self.iseaten


