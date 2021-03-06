import random

class Apples():
    def __init__(self):
        self.eaten = 0
        self.current = [50, 50]

    # Check if an apple has be eaten
    def checkAppleEaten(self, x, y, width, heigth, interface_heigth, obstacles):
        # If yes, increment score, snake size, apples eaten and set a new random position for apple
        if x == self.current[0] and y == self.current[1]:
            self.eaten += 1
            x = random.randint(1,
                                   width / 10) * 10 - 10  # Eg : between 1 and 30 so 30*10 = 300, to be sure to works with multiples of 10
            y = random.randint(1, int(heigth-interface_heigth) / 10) * 10 - 10 + interface_heigth # To be sure apple don't spawn in interface

            # An apple cannot appear in an obstacle
            while [x, y] in obstacles:
                x = random.randint(1,
                                   width / 10) * 10 - 10  # Eg : between 1 and 30 so 30*10 = 300, to be sure to works with multiples of 10
                y = random.randint(1, int(
                    heigth - interface_heigth) / 10) * 10 - 10 + interface_heigth  # To be sure apple don't spawn in interface
            self.current = [x, y]
            return True
        else:
            return False

