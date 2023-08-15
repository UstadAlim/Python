import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 11))
        self.setToolTip('Bu bir sade ve yungul penceredir')


        btn = QPushButton('Sevimli duymecik', self)
        btn.setToolTip('Bu bir duyme idi ve o sechildi')
        btn.resize(btn.sizeHint())
        btn.move(120, 25)

        self.setGeometry(300, 300, 350, 80)
        self.setWindowTitle('Tooltips')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

