import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDesktopWidget, QPushButton, QHBoxLayout, QGridLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QIcon, QPixmap, QColor, QPainter, QBrush
import keyboard

from snake import Snake
from apple import Apples

class Window(QWidget):
    layout = QGridLayout()
    snake = Snake()
    apples = Apples()

    # Init our UI
    def __init__(self):
        super().__init__()
        self.initUI()

    # Init our window
    def initUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Ma fenêtre")

        self.displayActionButtons()
        self.displayInformations()
        self.setLayout(self.layout)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        if self.snake.direction == 'X':
            self.drawInit(qp)
        elif self.snake.direction in 'LRDU':
            self.progressGame(qp)
        self.drawApples(qp)
        qp.end()

    def drawInit(self, qp):
        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        # Default snake position
        qp.setBrush(QColor(9, 106, 9))
        qp.drawRect(10, 10, 10, 10)
        # Default apple position
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(50, 50, 10, 10)

    def drawApples(self, qp):
        qp.setBrush(QColor(255, 0, 0))
        qp.drawRect(self.apples.current[0], self.apples.current[1], 10, 10)

    def displayActionButtons(self):
        # Action buttons
        leftButton = QPushButton("Left")
        rightButton = QPushButton("Right")
        upButton = QPushButton("Up")
        downButton = QPushButton("Down")

        leftButton.clicked.connect(self.leftButtonAction)
        rightButton.clicked.connect(self.rightButtonAction)
        upButton.clicked.connect(self.upButtonAction)
        downButton.clicked.connect(self.downButtonAction)

        self.layout.addWidget(leftButton, 1, 0)
        self.layout.addWidget(rightButton, 1, 2)
        self.layout.addWidget(upButton, 0, 1)
        self.layout.addWidget(downButton, 3, 1)

    def displayInformations(self):
        label = QLabel('Score : '+str(self.apples.eaten*100))
        self.layout.addWidget(label, 0, 0)

    def leftButtonAction(self):
        print('Left click')
        self.snake.direction = 'L'
        self.update()

    def rightButtonAction(self):
        print('Right click')
        self.snake.direction = 'R'
        self.update()

    def upButtonAction(self):
        print('Up click')
        self.snake.direction = 'U'
        self.update()

    def downButtonAction(self):
        print('Down click')
        self.snake.direction = 'D'
        self.update()

    def progressGame(self, qp):
        color = QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        lastMove = self.snake.historic[-1]
        moveToDelete = self.snake.historic[0]
        print('MOVE TO DELETE : ')
        print(moveToDelete)
        print('LAST MOVE :')
        print(lastMove)
        # Adapt position of last move according to the direction selected
        if self.snake.direction == 'R':
            x = lastMove[0] + 10
            y = lastMove[1]
        elif self.snake.direction == 'L':
            x = lastMove[0] - 10
            y = lastMove[1]
        elif self.snake.direction == 'U':
            x = lastMove[0]
            y = lastMove[1] - 10
        elif self.snake.direction == 'D':
            x = lastMove[0]
            y = lastMove[1] + 10
        else:
            x = 0
            y = 0
        print('New move :')
        print(x, y)

        eaten = self.checkAppleEaten(x, y)

        if eaten == 0: # If apple not eaten, snake don't grow
            # Delete last move in historic
            self.snake.historic.pop(0)

        # Add new move to historic
        self.snake.historic.append([x, y])
        # Color each new rect
        qp.setBrush(QColor(9, 106, 9))
        for position in self.snake.historic:
            qp.drawRect(position[0], position[1], 10, 10)
        # Set new move to none
        self.snake.direction = "-"


    def checkAppleEaten(self, x, y):
        if x == self.apples.current[0] and y == self.apples.current[1]:
            self.snake.size = 2
            self.apples.eaten += 1
            x = random.randint(1, 30)*10
            y = random.randint(1, 30)*10
            self.apples.current = [x, y]
            return 1
        else:
            return 0

def main():
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

