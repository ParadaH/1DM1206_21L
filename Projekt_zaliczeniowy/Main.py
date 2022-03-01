import sys

from PyQt5.QtWidgets import QApplication
from App_window import App

if __name__ == '__main__':

    app = QApplication([])
    width, height = 800, 600
    accepted_formats = (".csv")
    tabs_app = App(width, height, accepted_formats)
    sys.exit(app.exec_())
