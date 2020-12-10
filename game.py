import pygame
import random

from snake import Snake
from apple import Apples

class Game():

    # Default objects
    snake = Snake()
    apples = Apples()
    window_width = 300
    window_heigth = 300

    def __init__(self):
        pygame.init() # Init our game
        self.window = pygame.display.set_mode((self.window_width, self.window_heigth)) # Display our window to 300*300
        self.window.fill((255, 255, 255)) # Fill our window of white
        pygame.display.update() # Update our window
        pygame.display.set_caption('Jeu du snake')
        self.handleGame() # Launch game
        pygame.quit()

    def handleGame(self):
        gameOver = False # By default, no game over
        clock = pygame.time.Clock() # Setup our clock
        while not gameOver: # While we're not in game over
            for event in pygame.event.get(): # Check for event
                if event.type == pygame.QUIT: # If quit event, set game over to true
                    gameOver = True
                elif event.type == pygame.KEYDOWN: # If a key is pressed, we check for it
                    self.handleKeyPressed(event)
            # Handle display
            moveToDelete = self.moveSnake() # We setup our next move and retrieve the previous move to delete
            self.displaySnake(moveToDelete) # We will display our snake and remove our move to delete
            self.displayApple() # We display our apple
            gameSpeed = self.snake.handleRapidity() # Handle snake rapidity according to his size + set a speed limit
            clock.tick(gameSpeed) # Our clock freezing game

    # Change snake direction according to the key selected
    def handleKeyPressed(self, event):
        if event.key == pygame.K_LEFT:
            self.snake.direction = 'L'
        elif event.key == pygame.K_RIGHT:
            self.snake.direction = 'R'
        elif event.key == pygame.K_UP:
            self.snake.direction = 'U'
        elif event.key == pygame.K_DOWN:
            self.snake.direction = 'D'

    # Moving our snake
    def moveSnake(self):
        lastMove = self.snake.historic[-1] # Position of the head of the snake
        moveToDelete = self.snake.historic[0]
        # Retrieve the x and y of the next move
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

        eaten = self.checkAppleEaten(x, y) # Check if the snake ate an apple
        # If not, remove his tail, if yes, keep it ( the snake will have +1 length)
        if eaten == False:
            self.snake.historic.pop(0)
        # Add his new position on his historic
        self.snake.historic.append([x, y])
        return moveToDelete

    # Display the snake
    def displaySnake(self, moveToDelete):
        green = (9, 106, 9)
        white = (255, 255, 255)
        # Remove his tail
        pygame.draw.rect(self.window, white, [moveToDelete[0], moveToDelete[1], 10, 10])
        # Print on all of his positions
        for position in self.snake.historic:
            pygame.draw.rect(self.window, green, [position[0], position[1], 10, 10])
        pygame.display.update()

    # Display apple according to self.apples
    def displayApple(self):
        red = (255, 0, 0)
        pygame.draw.rect(self.window, red, [self.apples.current[0], self.apples.current[1], 10, 10])

    # Check if an apple has be eaten
    def checkAppleEaten(self, x, y):
        # If yes, increment score, snake size, apples eaten and set a new random position for apple
        if x == self.apples.current[0] and y == self.apples.current[1]:
            self.snake.size += 1
            self.apples.eaten += 1
            x = random.randint(1, self.window_width/10)*10-10 # Eg : between 1 and 30 so 30*10 = 300, to be sure to works with multiples of 10
            y = random.randint(1, self.window_heigth/10)*10-10
            self.apples.current = [x, y]
            return 1
        else:
            return 0

if __name__ == '__main__':
    Game()
