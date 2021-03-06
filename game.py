import pygame
import math

from snake import Snake
from apple import Apples
from scoreboard import Scoreboard
from obstacle import Obstacles
from bonus import Bonus


class Game():
    # Default objects
    apples = Apples()
    obstacles = Obstacles()
    window_width = 300
    window_heigth = 300
    interface_heigth = 30
    scoreBoard = Scoreboard()
    bonus = Bonus()

    def __init__(self):
        self.snake = Snake(self.interface_heigth)
        pygame.init()  # Init our game
        self.window = pygame.display.set_mode((self.window_width, self.window_heigth))  # Display our window to 300*300
        self.window.fill((255, 255, 255))  # Fill our window of white
        pygame.display.update()  # Update our window
        pygame.display.set_caption('Jeu du snake')
        restart = True
        # Loop if the player restart
        while restart:
            self.handleStartMenu()  # Launch menu
            self.handleGame()  # Launch game
            self.handleGameOverMenu()  # Display game over tab
        pygame.quit()

    def handleStartMenu(self):

        gameStart = False  # By default the game don't start
        background = pygame.image.load('assets/snake2.jpg')
        background = pygame.transform.scale(background, (300, 300))
        while not gameStart:
            self.window.blit(background, (0, 0))
            play_button = pygame.image.load('assets/button.png')  # We get ur image for the button from the assets rep
            play_button = pygame.transform.scale(play_button, (100, 50))
            play_button_rect = play_button.get_rect()
            play_button_rect.x = math.ceil(self.window_width / 3)
            play_button_rect.y = math.ceil(self.window_heigth / 2.5)
            self.window.blit(play_button, play_button_rect)  # print ur button
            font_style = pygame.font.SysFont(None, int(self.window_width / 10))
            font_style_2 = pygame.font.SysFont(None, int(self.window_width / 13))
            name = font_style.render(self.scoreBoard.playerName, True, (0, 0, 0))  # create a variable for the name of the player
            # create a message to warn the user he must give us a name
            msg_name = font_style_2.render("Veuillez saisir votre pseudo: ", True, (0, 0, 0))
            self.window.blit(msg_name, [self.window_width / 4.5, self.window_heigth / 4])  # print the message
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
            self.snake.handleRapidity()  # Handle snake rapidity according to his size + set a speed limit
            moveToDelete = self.handleMovement() # We setup our next move and retrieve the previous move to delete
            gameOver = self.handleGameOver()
            self.displaySnake(moveToDelete) # We will display our snake and remove our move to delete
            self.displayApple() # We display our apple
            self.displayInterface() # We display score and lives
            self.displayObstacle() # We display our obstacles
            self.displayBonus() # We display our bonuses
            pygame.display.update()
            clock.tick(self.snake.velocity) # Our clock freezing game

    # Handle if it's a game over or not
    def handleGameOver(self):
        # Check if the user died
        died = self.snake.checkDeath(self.window_width, self.window_heigth, self.interface_heigth, self.obstacles.obstacles)
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
                                            self.interface_heigth, self.obstacles.obstacles)  # Check if the snake ate an apple
        # If not, remove his tail, if yes, keep it ( the snake will have +1 length)
        if eaten == False:
            self.snake.historic.pop(0)
        else:
            self.snake.size += 1
            self.scoreBoard.playerScore += 100
        # Handle bonus
        self.handleBonus(x, y)
        # Add his new position on his historic
        self.snake.historic.append([x, y])
        return moveToDelete

    # Handle bonus gestion
    def handleBonus(self, x, y):
        # If bonuses not actives or displayed, try to make it spawn
        if not self.bonus.displayed and not self.bonus.active:
            self.bonus.spawnBonus(self.window_width, self.window_heigth, self.interface_heigth)
        else:
            if len(self.bonus.current) == 2:
                self.bonus.checkBonusEaten(x, y) # Check if eaten
                self.bonus.waiting -= 1
            if self.bonus.active: # Switch effect according to the bonus type
                if self.bonus.type == 'speed+':
                    self.snake.velocity = self.snake.velocity*3
                elif self.bonus.type == 'speed-':
                    self.snake.velocity = self.snake.velocity/3
                elif self.bonus.type == 'score+':
                    self.scoreBoard.playerScore += 500
                    self.bonus.duration = 0
                elif self.bonus.type == 'score-':
                    self.scoreBoard.playerScore -= 500
                    self.bonus.duration = 0
                # Handle bonus duration, instant for scores, 30 ticks for speed
                if self.bonus.duration > 0:
                    self.bonus.duration -= 1
                else:
                    self.bonus.active = False

            # If we waited too long for a bonus, it's gone
            if self.bonus.waiting == 0:
                pygame.draw.rect(self.window, (255, 255, 255), [self.bonus.current[0], self.bonus.current[1], 10, 10])
                self.bonus.active = False
                self.bonus.current = []
                self.bonus.displayed = False
                
    # Display bonus method
    def displayBonus(self):
        if len(self.bonus.current) == 2:
            pygame.draw.rect(self.window, self.bonus.color, [self.bonus.current[0], self.bonus.current[1], 10, 10])

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

    # Display obstacles
    def displayObstacle(self):
        black = (0, 0, 0)
        # Handle if we add obstacle
        if self.snake.size == self.obstacles.dernierPalier:
            self.obstacles.ajouterObstacle(self.window_width, self.window_heigth, self.interface_heigth, self.apples.current)
            self.obstacles.dernierPalier += 3
        # Display obstacles
        for i in self.obstacles.obstacles:
            pygame.draw.rect(self.window, black, [i[0], i[1], 10, 10])

    # Handle game over menu
    def handleGameOverMenu(self):
        restart = False  # create a local variable restart
        background = pygame.image.load('assets/snake.jpg')
        background = pygame.transform.scale(background, (300, 300))
        self.window.blit(background, (0, 0))
        self.handleScoreBoard()  # Handle scoreboard
        while not restart:
            font_style = pygame.font.SysFont(None, int(self.window_width/10))
            mesg = font_style.render("Game Over", True, (255, 0, 0))
            self.window.blit(mesg, [self.window_width / 3, self.window_heigth / 2])

            # Create and set a position to ur restart button
            restart_button = pygame.image.load('assets/restart.png')
            restart_button = pygame.transform.scale(restart_button, (100, 50))
            restart_button_rect = restart_button.get_rect()
            restart_button_rect.x = math.ceil(self.window_width / 3)
            restart_button_rect.y = math.ceil(self.window_heigth / 1.3)
            self.window.blit(restart_button, restart_button_rect)  # print ur button

            # Create and set a quit button
            leave_button = pygame.image.load('assets/quit.png')
            leave_button = pygame.transform.scale(leave_button, (100, 50))
            leave_button_rect = leave_button.get_rect()
            leave_button_rect.x = math.ceil(self.window_width / 3)
            leave_button_rect.y = math.ceil(self.window_heigth / 1.7)
            self.window.blit(leave_button, leave_button_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # check if user want to leave
                    pygame.quit()  # close the game
                elif event.type == pygame.MOUSEBUTTONDOWN:  # check if the user is clicking with the mouse
                    #  check if he's clicking on the position of the restart button
                    if restart_button_rect.collidepoint(event.pos):
                        restart = True  # set restart is true
                    # check if he's clicking on the exit button
                    if leave_button_rect.collidepoint(event.pos):
                        pygame.quit()  # leave the game

        if restart:
            # if the player want to restart the game we reset his attribute
            self.scoreBoard.playerName = ''
            self.scoreBoard.playerScore = 0
            self.snake = Snake(self.interface_heigth)
            self.obstacles = Obstacles()
            self.apples = Apples()

    # Handle scoreboard display
    def handleScoreBoard(self):
        self.scoreBoard.writeScore() # Write the new score
        self.scoreBoard.readScoreBoard() # Read score board
        font_style = pygame.font.SysFont(None, int(self.window_width / 14))
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

