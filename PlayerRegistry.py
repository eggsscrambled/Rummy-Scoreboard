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

        self.playerRegisterBox.setMaxLength(20)

        self.addPlayerButton.clicked.connect(self.AddPlayer)    #Add player button
        self.removePlayerButton.clicked.connect(self.RemovePlayer)  #Remove player button

    def AddPlayer(self):
        global players
        NameUsed = False

        name = self.playerRegisterBox.text().strip() #Get name to text and remove whitespace
        name = name.title() #Format name


        if name != "":  #Ensure name cannot be empty


            for i in range (len(players)):
                nameToCheck = players[i].name   #Loop through player list and make sure that name is unique
                if(nameToCheck == name):
                    NameUsed = True

            if(NameUsed == False):  #If name is truly unique then add it to the list
                playerToRegister = Player(name)

                players.append(playerToRegister)    #Add instance of player to global array

                self.playerList.addItem(playerToRegister.name)      #Add name to list
                self.playerRegisterBox.clear()  #Clear input box
            else:
                NameUsed = False


    def RemovePlayer(self):
        global players
        item = self.playerList.currentItem()    #Get the name of the selected item
        name = item.text()

        for player in players:
            if name == player.name:     #Find the correct instance of Player to remove using names in list
                playerToRemove = player

        players.remove(playerToRemove)  #Remove from internal player list
        index = self.playerList.currentRow()
        self.playerList.takeItem(index) #Remove from UI list


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())