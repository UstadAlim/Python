import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QFormLayout, QLabel, QLineEdit, QWidget, QVBoxLayout, QMessageBox


class LoginDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        self.username = QLineEdit()
        self.password = QLineEdit()
        loginLayout = QFormLayout()
        loginLayout.addRow("Username", self.username)
        loginLayout.addRow("Password", self.password)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.check)
        self.buttons.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(loginLayout)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

    def check(self):
        if str(self.username.text()) == "foo" and str(self.password.text()) == "bar":
            self.accept()
        else:
            QMessageBox.warning(
                self, 'Error', 'Bad user or password')
            pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.label = QLabel()
        self.setCentralWidget(self.label)

    def setUsername(self, username):
        self.username = username
        self.label.setText("%s%s%s" % ("Username entered: ", self.username, "\npassword ok!"))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginDialog()
    if not login.exec_():
        sys.exit(-1)

    main = MainWindow()

    main.setUsername(login.username.text())
    main.show()

    sys.exit(app.exec_())




