from PlayerInfo import Player

import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

class ScoreboardWindow(QMainWindow):



    def __init__(self):
        super().__init__()
        uic.loadUi("Scoreboard.ui", self)
