class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.pointsPerRound = []

    def AddPoints(self, pointsFromRound):
        self.score += pointsFromRound
        self.pointsPerRound.append(pointsFromRound)

    def GetCurrentScore(self):
        return self.score
