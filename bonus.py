import random
import time

class Bonus():
    def __init__(self):
        self.bonus1 = []
        self.bonuseaten = 0
        self.bonusx = random.randrange(0, 300,10)
        self.bonusy = random.randrange(0, 300,10)
        self.current = [self.bonusx, self.bonusy]
        self.lifetime = 30
        self.iseaten = False

    # Check if an apple has be eaten

    # def spawnBonus(self):
    #     if len(self.bonus1) == 0:
    #         randomBonus = random.init(10, 30)

    def checkBonusEaten(self, x, y, width, heigth):
        # If yes, increment score, snake size, apples eaten and set a new random position for apple
        if x == self.current[0] and y == self.current[1]:

            self.bonuseaten += 1
            self.iseaten = True
            return self.iseaten
        else:
            return self.iseaten
