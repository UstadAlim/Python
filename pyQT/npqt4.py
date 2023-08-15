import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):

        if e.button() == Qt.LeftButton:
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.RightButton:
            self.label.setText("mousePressEvent RIGHT")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
