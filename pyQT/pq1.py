from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.move(50, 50)

    def setupUI(self):
        self.btn = QPushButton()
        self.btn.setText("Registration")
        self.btn.move(400, 400)
        self.resize(400, 400)

        self.btn.show()
        self.btn.clicked.connect(dialog)

        self.setWindowTitle("My GAME")
        self.move(300,100)
        self.resize(700,700)
        self.lbl = QLabel('Persian Boy',self)
        self.lbl.move(300,10)
        self.lbl.resize(300,70)

        self.font = QFont()
        self.font.setFamily("Arail")
        self.font.setPointSize(15)
        self.font.setCapitalization(True)

        self.font.setBold(True)
        self.lbl.setFont(self.font)

def dialog():
     mbox = QMessageBox()
     mbox.setText("Registration panel")
     mbox.setDetailedText("Finish!")
     mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
     mbox.exec_()

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())




