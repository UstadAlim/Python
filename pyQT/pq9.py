from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MPP')
        self.setGeometry(200,100, 350, 250)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        dialog = QColorDialog(self)
        dialog.setCurrentColor(Qt.red)
        dialog.exec_()

        label = QLabel('MyColor',self)
        label.setGeometry(200,100, 100, 60)
        label.setWordWrap(True)
        label.setStyleSheet("QLabel"
                            "{"
                            "border : 5px solid black;"
                            "}")

        color = Qt.darkBlue
        graphic = QGraphicsColorizeEffect(self)
        graphic.setColor(color)
        value = dialog.currentColor()
        label.setText("Selected color: "+str(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())



