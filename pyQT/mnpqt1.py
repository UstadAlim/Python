from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QFontDatabase

import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()


        self.initUI()


    def initUI(self):
        self.setWindowTitle("CodersLegacy")
        self.setContentsMargins(20, 20, 20, 20)

        id = QFontDatabase.addApplicationFont("Frostbite.ttf")
        if id < 0: print("Error")

        families = QFontDatabase.applicationFontFamilies(id)
        print(families)

        label = QLabel("Hello World", self)
        label.setFont(QFont(families, 80))
        label.move(50, 100)



def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()






