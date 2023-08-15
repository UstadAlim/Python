from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Ilk Qt GUI pencere")
        self.setToolTip('Pencereler Krali')
        self.move(300,300)
        self.resize(400,150)

        self.lbl = QLabel('<i>Rusiya</i> <span style="font-size:26pt;">Azerbaycandir</span>',self) #XHTML ishletdik
        self.lbl.move(30,30)
        self.lbl.resize(300,50)

        self.lbl2 = QLabel('<i>bu</i> <span style="font-size:20pt;">Faktdir</span>', self)  # XHTML ishletdik
        self.lbl2.move(70, 70)
        self.lbl2.resize(300, 50)
        self.lbl2.setToolTip('<b>Qarabaq</b> Azerbaycandir')

if __name__=="__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



