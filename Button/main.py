from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys

class Widget(QWidget):
    def __init__(self):
        super(Widget,self).__init__()
        loadUi("form.ui",self)


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.setWindowTitle("Button")
    widget.show()
    sys.exit(app.exec_())
 
