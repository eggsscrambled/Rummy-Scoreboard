class Player:


    def __init__(self, name): # Function to create a new player
        self.name = name
        self.score = 0
        self.pointsPerRound = []

    def AddPoints(self, pointsFromRound): # Adds to your total and adds to the round points array
        self.score += pointsFromRound
        self.pointsPerRound.append(pointsFromRound)

    def GetCurrentScore(self): # Returns the players current score
        return self.score


