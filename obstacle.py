import random

class Obstacles():
    def __init__(self):
        self.obstacles = [] # Set obstacles on empty
        self.dernierPalier = 3

    def ajouterObstacle(self, width, heigth, interface_heigth, currentApple):
        coordx = random.randint(interface_heigth/10, ((width - 30) / 10)) * 10
        coordy = random.randint(interface_heigth/10, ((heigth - 30) / 10)) * 10
        r = random.randint(0, 1)
        # Choose of obstacle direction
        # An obstacle cannot spawn in an appel
        if r == 0:
            while [coordx, coordy] == currentApple or [coordx, coordy + 10] == currentApple or [coordx,
                                                                                                coordy + 20] == currentApple:
                coordx = random.randint(interface_heigth / 10, ((width - 30) / 10)) * 10
                coordy = random.randint(interface_heigth / 10, ((heigth - 30) / 10)) * 10
            self.obstacles.append([coordx, coordy])
            self.obstacles.append([coordx, coordy + 10])
            self.obstacles.append([coordx, coordy + 20])
        else:
            while [coordx, coordy] == currentApple or [coordx + 10, coordy] == currentApple or [coordx + 20,
                                                                                                coordy] == currentApple:
                coordx = random.randint(interface_heigth / 10, ((width - 30) / 10)) * 10
                coordy = random.randint(interface_heigth / 10, ((heigth - 30) / 10)) * 10
            self.obstacles.append([coordx, coordy])
            self.obstacles.append([coordx + 10, coordy])
            self.obstacles.append([coordx + 20, coordy])