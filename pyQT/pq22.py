import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPixmap


class DragButton(QPushButton):

    def mouseMoveEvent(self, e):

        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)
            drag.exec_(Qt.MoveAction)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

        self.blayout = QHBoxLayout()

        for l in ['A', 'B', 'C', 'D']:
            btn = DragButton(l)
            self.blayout.addWidget(btn)

        self.setLayout(self.blayout)
        self.show()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        widget = e.source()

        for n in range(self.blayout.count()):
            w = self.blayout.itemAt(n).widget()
            if pos.x() < w.x() + w.size().width() // 2:
                self.blayout.insertWidget(n - 1, widget)
                break

        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())