from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor
import sys, random

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 350, 100)
        self.setWindowTitle('Colours')
        self.show()


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()


    def drawRectangles(self, qp):
        a1 = random.randint(1, 255)
        a2 = random.randint(1, 255)
        a3 = random.randint(1, 255)

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(a1, 20, a3))
        qp.drawRect(10, 5, 60, 60)

        qp.setBrush(QColor(a2, 80, 0, 160))
        qp.drawRect(130, 15, 120, 60)

        qp.setBrush(QColor(a3, 0, 90, 200))
        qp.drawRect(250, 35, 40, 60)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
