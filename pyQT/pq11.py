import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Button Panel')

layout = QGridLayout()
layout.addWidget(QPushButton('Open'),0,0)
layout.addWidget(QPushButton('Close'),0,1)
layout.addWidget(QPushButton('Exit'),0,2)

layout.addWidget(QPushButton('Cut'),1,0)
layout.addWidget(QPushButton('Copy'),1,1)
layout.addWidget(QPushButton('Paste'),1,2)

layout.addWidget(QPushButton('New'),2,0,1,3)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
