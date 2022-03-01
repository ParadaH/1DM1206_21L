from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon


class Error(QMessageBox):

    def __init__(self, msg):
        super().__init__()

        self.setIcon(QMessageBox.Critical)
        icon = QIcon()

        self.setWindowIcon(icon)
        self.setWindowTitle("Error!")
        self.setText(msg)
        self.exec_()
