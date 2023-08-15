import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Base Panel')

layout = QFormLayout()
layout.addRow('Name:', QLineEdit())
layout.addRow('Surename:', QLineEdit())
layout.addRow('Age:', QLineEdit())
layout.addRow('Job or Position:', QLineEdit())

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
