from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Nagil")

    btn1 = QPushButton("Melikmemmed")
    btn2 = QPushButton("Aq atli oqlan")
    btn3 = QPushButton("Tenbel Ehmed")

    ''' hbox=QHBoxLayout(w)
    hbox.addWidget(btn1)
    hbox.addWidget(btn2)
    hbox.addWidget(btn3)'''

    vb = QVBoxLayout(w)
    vb.addWidget(btn1)
    vb.addWidget(btn2)
    vb.addWidget(btn3)


    w.show()
    sys.exit(app.exec_())





