import sys
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Salamlama penceresi'
        self.left = 200
        self.top = 180
        self.width = 240
        self.height = 280
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Ish gedir')

        self.textbox = QLineEdit(self)
        self.textbox.move(30, 30)
        self.textbox.resize(200, 20)

        self.button = QPushButton('Click me', self)
        self.button.move(15, 85)

        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        textboxValue = self.textbox.text()
        self.statusBar().showMessage(textboxValue)
        QMessageBox.question(self,'Pencere',"Daxil olunub: "+textboxValue,
                             QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        self.statusBar().showMessage("")


if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())








