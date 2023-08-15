import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Daxiletme')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Surename:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Job or Position:', QLineEdit())
        dlgLayout.addLayout(formLayout)

        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok | QDialogButtonBox.Abort)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())