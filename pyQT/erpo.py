import sys

from PyQt6.QtWidgets import (QWidget, QLineEdit, QApplication, QComboBox, QFormLayout, QLabel)

class combo(QComboBox):

    def __init__(self, title, parent):
        super(combo, self).__init__(parent)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        lo = QFormLayout()
        lo.addRow(QLabel("Burada muxtelif metn bloklar olacaq"))
        edit = QLineEdit()
        edit.setDragEnabled(True)

        com = combo("Button", self)
        lo.addRow(edit, com)

        self.setLayout(lo)
        self.setWindowTitle('Simple drag & drop')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec()


if __name__ == '__main__':
    main()




