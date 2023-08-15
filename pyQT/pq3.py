from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
import sys

def dialog():
    mbox = QMessageBox()
    mbox.setText("Qeydiyyat penceresi")
    mbox.setDetailedText("Bu chox iri bir paneldir onun yuzlerle metodu var")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle("Xeberdar")

    label = QLabel(w)
    label.setText("Balaxani zibilliyi indi debli yerdir")
    label.move(100, 120)
    label.show()

    btn = QPushButton(w)
    btn.setText("Limonka")
    btn.move(120,150)
    btn.show()
    btn.clicked.connect(dialog)

    w.show()
    sys.exit(app.exec_())





