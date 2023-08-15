import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QLabel, QMainWindow, QVBoxLayout
from PyQt5.QtCore import Qt, QMimeData, pyqtSignal
from PyQt5.QtGui import QDrag, QPixmap

class DragItem(QLabel):



class DragWidget(QWidget):


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drag = DragWidget(orientation=Qt.Orientation.Vertical)
        for n, l in enumerate(['A', 'B', 'C', 'D']):
            item = DragItem(l)
            item.set_data(n)
            self.drag.add_item(item)
            




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

