import pygame
import time
import math

from snake import Snake
from apple import Apples
from scoreboard import Scoreboard
from obstacle import Obstacles


class Game():
    # Default objects
    apples = Apples()
    obstacles = Obstacles()
    window_width = 300
    window_heigth = 300
    interface_heigth = 30
    snake = Snake()
    scoreBoard = Scoreboard()

    def __init__(self):
        pygame.init()  # Init our game
        self.window = pygame.display.set_mode((self.window_width, self.window_heigth))  # Display our window to 300*300
        self.window.fill((255, 255, 255))  # Fill our window of white
        pygame.display.update()  # Update our window
        pygame.display.set_caption('Jeu du snake')
        restart = True
        while restart:
            self.handleStartMenu()  # Launch menu
            self.handleGame()  # Launch game
            restart = self.handleGameOverMenu()  # Display game over tab
        pygame.quit()

    def handleStartMenu(self):

        gameStart = False  # By default the game don't start

        while not gameStart:
            self.window.fill((255, 255, 255))
            play_button = pygame.image.load('assets/button.png')  # We get ur image for the button from the assets rep
            play_button = pygame.transform.scale(play_button, (100, 50))
            play_button_rect = play_button.get_rect()
            play_button_rect.x = math.ceil(self.window_width / 3)
            play_button_rect.y = math.ceil(self.window_heigth / 2.5)
            self.window.blit(play_button, play_button_rect)  # print ur button
            font_style = pygame.font.SysFont(None, int(self.window_width / 10))
            font_style_2 = pygame.font.SysFont(None, int(self.window_width / 15))
            name = font_style.render(self.scoreBoard.playerName, True, (0, 0, 0))  # create a variable for the name of the player
            # create a message to warn the user he must give us a name
            msg_name = font_style_2.render("Veuillez saisir votre pseudo: ", True, (0, 0, 0))
            self.window.blit(msg_name, [self.window_width / 3.5, self.window_heigth / 4])  # print the message
            self.window.blit(name, [self.window_width / 3, self.window_heigth / 3])  # print the name in real time
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # check if the user want to leave the game
                    pygame.quit()  # if the user try to leave we close the game
                elif event.type == pygame.KEYDOWN:  # If a key is pressed, we check for it
                    # check if the last input is a valid one (the code ascii is between 0 and 126) and it's not the
                    if 0 <= event.key <= 126 and event.key != 8:
                        self.scoreBoard.playerName += chr(event.key)  # We get the new input into the player_name
                        # check if the user want to delete the last input (and his name have at least one char)
                    elif event.key == 8 and self.scoreBoard.playerName != "":
                        self.scoreBoard.playerName = self.scoreBoard.playerName[:-1]  # delete the last char
                elif event.type == pygame.MOUSEBUTTONDOWN:  # check if the user is clicking with the mouse
                    # if it's clicking on the image of the button and the player have a valid name (not null)
                    if play_button_rect.collidepoint(event.pos) and self.scoreBoard.playerName != "":
                        gameStart = True  # we set the game start on true
        if gameStart:  # if the game start we clean the screen before printing the game
            self.window.fill((255, 255, 255))
            pygame.display.update()

    def handleGame(self):
        gameOver = False # By default, no game over
        clock = pygame.time.Clock() # Setup our clock
        while not gameOver: # While we're not in game over
            for event in pygame.event.get(): # Check for event
                if event.type == pygame.QUIT: # If quit event, set game over to true
                    pygame.quit()
                elif event.type == pygame.KEYDOWN: # If a key is pressed, we check for it
                    self.handleKeyPressed(event)
            # Handle display
            moveToDelete = self.handleMovement() # We setup our next move and retrieve the previous move to delete
            gameOver = self.handleGameOver()
            self.displaySnake(moveToDelete) # We will display our snake and remove our move to delete
            self.displayApple() # We display our apple
            self.displayInterface() # We display score and lives
            self.displayObstacle() # We display our obstacles
            self.snake.handleRapidity() # Handle snake rapidity according to his size + set a speed limit
            pygame.display.update()
            clock.tick(self.snake.velocity) # Our clock freezing game

    # Handle if it's a game over or not
    def handleGameOver(self):
        died = self.snake.checkDeath(self.window_width, self.window_heigth, self.interface_heigth)
        # If snake has no lives, set game over
        if self.snake.lives == 0:
            return True
        else:
            # If snake died, have to respawn him
            if died == True:
                self.window.fill((255, 255, 255))
                self.snake.respawn(self.window_width, self.interface_heigth)
            return False

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
    def handleMovement(self):
        moveToDelete = self.snake.historic[0]  # Tail of the snake
        [x, y] = self.snake.moveSnake(self.interface_heigth)  # Next position of the snake
        eaten = self.apples.checkAppleEaten(x, y, self.window_width, self.window_heigth,
                                            self.interface_heigth)  # Check if the snake ate an apple
        # If not, remove his tail, if yes, keep it ( the snake will have +1 length)
        if eaten == False:
            self.snake.historic.pop(0)
        else:
            self.snake.size += 1
            self.scoreBoard.playerScore += 100
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

    # Display apple according to self.apples
    def displayApple(self):
        red = (255, 0, 0)
        pygame.draw.rect(self.window, red, [self.apples.current[0], self.apples.current[1], 10, 10])

    # Display lives and score
    def displayInterface(self):
        pygame.draw.rect(self.window, (175, 175, 175), [0, 0, self.window_width, 30])
        font_style = pygame.font.SysFont(None, int(self.window_width / 15))
        lives = font_style.render("Vies : "+str(self.snake.lives), True, (0, 0, 0))
        score = font_style.render("Score : " + str(self.scoreBoard.playerScore), True, (0, 0, 0))
        self.window.blit(score, [5, 5])
        self.window.blit(lives, [int(self.window_width/1.3), 5])

    def displayObstacle(self):
        black = (0, 0, 0)

        self.obstacles.initialiserCoordonnees(self.window_width, self.window_heigth)

        if self.snake.size == self.obstacles.dernierPalier:
            self.obstacles.ajouterObstacle(self.window_width, self.window_heigth)
            self.obstacles.dernierPalier += 10

        for i in range(0, (len(self.obstacles.obstacles)-1), 2):

            pygame.draw.rect(self.window, black, [self.obstacles.obstacles[i+0], self.obstacles.obstacles[i+1], 10, 10])

    # Handle game over menu
    def handleGameOverMenu(self):
        self.window.fill((255, 255, 255))
        font_style = pygame.font.SysFont(None, int(self.window_width / 10))
        self.handleScoreBoard() # Handle scoreboard
        font_style = pygame.font.SysFont(None, int(self.window_width/10))
        mesg = font_style.render("Game Over", True, (255, 0, 0))
        self.window.blit(mesg, [self.window_width / 3, self.window_heigth / 2])
        pygame.display.update()
        time.sleep(10)

    def handleScoreBoard(self):
        self.scoreBoard.writeScore() # Write the new score
        self.scoreBoard.readScoreBoard() # Read score board
        font_style = pygame.font.SysFont(None, int(self.window_width / 16))
        i = 1
        # Write data in our menu
        for element in self.scoreBoard.scoreBoard:
            # For each element, display player name and score
            score = font_style.render(str(i)+" "+element["name"]+" "+str(element["score"]), True, (0, 0, 0))
            self.window.blit(score, [5, i*12])
            i+= 1
        pygame.display.update()

def main():
    Game()

if __name__ == '__main__':
    main()

