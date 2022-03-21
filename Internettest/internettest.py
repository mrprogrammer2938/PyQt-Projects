# pip install PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys,subprocess,platform


system = platform.system()

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/page.ui",self)
        self.setWindowTitle("Ping Test")
        self.setFixedSize(737,684)
        self.key = QShortcut(QKeySequence("Return"),self)
        self.key.activated.connect(self.start_scan)
        self.key2 = QShortcut(QKeySequence("Enter"),self)
        self.key2.activated.connect(self.start_scan)
        self.scan_btn.clicked.connect(self.start_scan)
        self.exit_btn.clicked.connect(self.close)
        self.clear_btn.clicked.connect(self.clear_txt)
        self.y = False
    def start_scan(self):
        if system == "Windows":
            att = subprocess.getoutput(f"ping {self.url.text()}")
            if (self.y==True):
                self.txt.insertPlainText(f"\n\n{att}")
            else:
                self.txt.insertPlainText(att)
                self.y = True
        elif system == "Linux":
            att = subprocess.getoutput(f"ping {self.url.text()}")
            if (self.y==True):
                self.txt.insertPlainText(f"\n\n{att}")
            else:
                self.txt.insertPlainText(att)
                self.y = True
    def clear_txt(self):
        self.txt.clear()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Ping Test")
    win = Window()
    win.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
