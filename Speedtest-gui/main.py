#!/usr/bin/python3
# Speed Test v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from speedtest import Speedtest
import sys

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/page.ui",self)
        self.setWindowTitle("Speed Test")
        self.setWindowIcon(QIcon("./icon/speed-icon.png"))
        self.setFixedSize(400,400)
        self.scan_btn.clicked.connect(self.scan)
        
    def scan(self):
        speed = Speedtest()
        download = speed.download()
        upload = speed.upload()
        self.label_download.setText(str(download))
        self.label_upload.setText(str(upload))
        
def main():
    # Speed Test v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Speed Test")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
