import random
import time

class Bonus():
    def __init__(self):
        self.type = ''
        self.active = False
        self.displayed = False
        self.duration = 30
        self.waiting = 30
        self.color = (0, 0, 0)
        self.current = []

    # Settle spawn bonus if it's not spawned yet
    def spawnBonus(self, width, heigth, interface_heigth):
        r = random.randint(1, 10) # 10% of chance
        if r == 1:
            self.displayed = True # Set displayed of true and determine the type of bonus
            type = random.randint(1, 4)
            if type == 1: # Less speed
                self.type = 'speed-'
                self.color = (0, 0, 255)
            elif type == 2: # More Speed
                self.type = 'speed+'
                self.color = (255, 127, 0)
            elif type == 3: # +500 score
                self.type = 'score+'
                self.color = (0, 0, 255)
            elif type == 4: # -500 score
                self.type = 'score-'
                self.color = (255, 127, 0)
            # Determine random position
            x = random.randint(1,
                               width / 10) * 10 - 10  # Eg : between 1 and 30 so 30*10 = 300, to be sure to works with multiples of 10
            y = random.randint(1, int(
                heigth - interface_heigth) / 10) * 10 - 10 + interface_heigth  # To be sure apple don't spawn in interface
            self.current = [x, y]
            self.waiting = 30

    def checkBonusEaten(self, x, y):
        # If yes, Set bonus to active
        if x == self.current[0] and y == self.current[1]:
            self.active = True
            self.current = []
            self.duration = 30
            self.displayed = False
            return True
        else:
            return False


