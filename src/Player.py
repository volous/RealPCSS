class Player:

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.wins = 0
        self.losses = 0
        self.currency = 100

    def playerWins(self):
        self.wins += 1

    def playerLoses(self):
        self.losses += 1


playerOne = Player("volous", "Bendoveruwu")
playerTwo = Player("Luzon", "test")
playerThree = Player("Fantanious", "nemtkodeord")

playerTwo.playerWins()
playerThree.playerLoses()

print(playerTwo.wins)
print("Player Three has", playerThree.losses, "loss(es)")


def player(self):
    pass