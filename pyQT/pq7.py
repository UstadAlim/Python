import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Salamlama penceresi'
        self.left = 200
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        exitButton = QAction(QIcon('exit-24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())




