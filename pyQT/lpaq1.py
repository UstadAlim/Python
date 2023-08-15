from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt
import sys, random


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setMinimumSize(50, 50)
        self.setGeometry(300, 300, 550, 500)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.GlobalColor.red)
        size = self.size()

        for i in range(1200):
            x1 = random.randint(1, size.width()/2)
            y1 = random.randint(1, size.height()/2)

            x2 = random.randint(1, size.width() -1)
            y2 = random.randint(1, size.height() -2)

            qp.drawLine(x1, y1, x2, y2)


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()