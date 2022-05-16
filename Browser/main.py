#!/usr/bin/python3
# Browser In PyQt
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("Webbrowser")
        self.setWindowIcon(QIcon("./icon/browser-icon.png"))
        self.setGeometry(300,50,1400,800)
        
        try:
            self.browser = QWebEngineView(self)
            self.browser.setUrl(QUrl("https://google.com"))
            self.setCentralWidget(self.browser)
        except (Exception,):
            pass
        
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Webbrowser")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
