import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QFont
from PyQt6.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.text = "Ziya"

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Drawing text')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):
        qp.setPen(QColor(181, 34, 3))
        qp.setFont(QFont('Decorative', 60))
        qp.drawText(event.rect(), Qt.AlignmentFlag.AlignCenter, self.text)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
