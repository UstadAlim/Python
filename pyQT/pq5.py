from PyQt5.QtWidgets import *
import sys

class Exampla(QWidget):
    def __init__(self):
        super.__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        qbtn.move(50, 50)

def main():
    app = QApplication(sys.argv)


if __name__ == "__main__":
    main()
