import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Ellada Shop")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


