import random

from random import choice

class Obstacles():
    def __init__(self):
        self.obstacles = []
        self.initialisation = False
        self.dernierPalier = 10

    def ajouerObstacleInit(self, x, y):
        self.obstacles.append(x)
        self.obstacles.append(y)

    def ajouterObstacle(self, width, heigth):
        coordx = random.randint(0, ((width - 30) / 10)) * 10
        coordy = random.randint(0, ((heigth - 30) / 10)) * 10
        self.obstacles.append(coordx)
        self.obstacles.append(coordy)
        self.obstacles.append(coordx)
        self.obstacles.append(coordy + 10)
        self.obstacles.append(coordx)
        self.obstacles.append(coordy + 20)

    def initialiserCoordonnees(self, width, heigth):

        while self.initialisation != True:

            coordx = random.randint(0, ((width-30) / 10)) * 10
            coordy = random.randint(0, ((heigth-30) / 10)) * 10
            self.ajouerObstacleInit(coordx, coordy)
            self.ajouerObstacleInit(coordx, coordy+10)
            self.ajouerObstacleInit(coordx, coordy+20)

            coorda = random.randint(0, ((width-30) / 10)) * 10
            coordb = random.randint(0, ((heigth-30) / 10)) * 10
            self.ajouerObstacleInit(coorda, coordb)
            self.ajouerObstacleInit(coorda + 10, coordb)
            self.ajouerObstacleInit(coorda + 20, coordb)

            coordc = random.randint(0, ((width-30) / 10)) * 10
            coordd = random.randint(0, ((heigth-30) / 10)) * 10
            self.ajouerObstacleInit(coordc, coordd)
            self.ajouerObstacleInit(coordc + 10, coordd)
            self.ajouerObstacleInit(coordc + 20, coordd)

            self.initialisation = True