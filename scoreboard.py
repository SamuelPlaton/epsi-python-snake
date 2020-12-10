
class Scoreboard():

    def __init__(self):
        self.playerName = '' # Player name
        self.playerScore = 0 # Player score, 0 by default
        self.scoreBoard = []
        self.readScoreBoard()

    # Write new score in file
    def writeScore(self):
        file = open("data/scoreboard.txt", 'a')
        file.write(str(self.playerName)+":"+str(self.playerScore)+"\n")
        file.close()

    def readScoreBoard(self):
        file = open("data/scoreboard.txt", 'r')
        scoreboard = [] # Default scoreboard, empty
        line = file.readline() # Our file line
        while line:
            [name, score] = line.split(":") # Retrieve name and score
            dict = { "name" : name, "score": int(score)} # Settle a dict
            scoreboard.append(dict) # Add our dict
            line = file.readline() # Get our new line
        scoreboard = sorted(scoreboard, key= lambda k: k["score"]) # Sort list by score
        scoreboard.reverse() # Reverse to get the best scores
        self.scoreBoard = scoreboard[:10] # Get the 10 best
        file.close()