from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
import sys
def ferqli():
    w1 = QWidget()
    w1.move(300, 180)
    w1.resize(300, 300)
    w1.setWindowTitle("Pencere 2")
    w1.show()
    w1.exec_()


def yeni():
    label = QLabel(w)
    label.setText("Balaxani zibilliyi indi debli yerdir")
    label.move(100, 120)
    label.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("Pencere 1")

    btn = QPushButton(w)
    btn.setText("Olsun")
    btn.move(120, 150)
    btn.show()
    btn.clicked.connect(ferqli)

    w.show()
    sys.exit(app.exec_())
