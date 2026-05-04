from PlayerInfo import Player

import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

players = []

class MainWindow(QMainWindow):



    def __init__(self):
        super().__init__()
        print()
        uic.loadUi("PlayerInput.ui", self)


        self.addPlayerButton.clicked.connect(self.AddPlayer)
        self.removePlayerButton.clicked.connect(self.RemovePlayer)

    def AddPlayer(self):
        global players
        name = self.playerRegisterBox.toPlainText().strip()
        playerToRegister = Player(name)

        players.append(playerToRegister)    #Add instance of player to global array

        self.playerList.addItem(playerToRegister.name)      #Add name to list
        self.playerRegisterBox.clear()  #Clear input box


    def RemovePlayer(self):
        global players
        item = self.playerList.currentItem()
        name = item.text()

        for player in players:
            if name == player.name:
                playerToRemove = player

        players.remove(playerToRemove)
        index = self.playerList.currentRow()
        self.playerList.takeItem(index)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())