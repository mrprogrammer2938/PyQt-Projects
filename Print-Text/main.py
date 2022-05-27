#!/usr/bin/python3
# Print-Text v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("Print Text")
        self.setGeometry(500,100,900,700)
        self.txt = QTextEdit(self)
        self.txt.setFont(QFont("Arial",13))
        self.setCentralWidget(self.txt)
        menu = QMenuBar(self)
        self.setMenuWidget(menu)
        filemenu = menu.addMenu("Options")
        viewmenu = menu.addMenu("View")
        print_action = QAction("Print",self)
        print_action.setShortcut("Ctrl+p")
        print_action.setWhatsThis("Print")
        print_action.setStatusTip("Print")
        print_action.triggered.connect(self.printer)
        exit_action = QAction("Exit",self)
        exit_action.setShortcut("Alt+f4")
        exit_action.setWhatsThis("Exit")
        exit_action.setStatusTip("Exit")
        exit_action.triggered.connect(self.close)
        filemenu.addAction(print_action)
        filemenu.addSeparator()
        filemenu.addAction(exit_action)
        font_action = QAction("Set Font",self)
        font_action.setWhatsThis("Set Font")
        font_action.setStatusTip("Set Font")
        font_action.triggered.connect(self.set_font)
        viewmenu.addAction(font_action)

    def set_font(self):
        font_, ok = QFontDialog().getFont()
        if ok:
          self.txt.setFont(font_)

    def printer(self):
        prt = QPrintDialog(self)
        if prt.exec_():
          self.txt.print_(prt.printer_())


def main():
    # Print Text
    app = QApplication(sys.argv)
    app.setApplicationName("Print Text")
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
  main()
