#!/usr/bin/python3
# Instagram-Downloader v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from instaloader.instaloader import Instaloader,InstaloaderException
import sys

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/page.ui",self)
        self.setWindowTitle("Instagram-Downloader")
        self.setWindowIcon(QIcon("./icon/instagram-downloader-icon.png"))
        self.setFixedSize(525,419)
        self.download_btn.clicked.connect(self.download)
        
    def download(self):
        try:
            self.username = self.user_inp.text()
            ins = Instaloader()
            ins.download_profile(self.username,profile_pic_only=True)
            mess = QMessageBox(self)
            mess.setStyleSheet("color: #fff;")
            mess.setWindowTitle("Instagram-Downloader/Error")
            mess.setIcon(QMessageBox.information)
            mess.setText(f"{self.username} Profile Has Downloaded!")
            mess.exec_()
        except (Exception,InstaloaderException,):
            mess_r = QMessageBox(self)
            mess_r.setStyleSheet("color: #fff;")
            mess_r.setWindowTitle("Instagram-Downloader/Error")
            mess_r.setIcon(QMessageBox.Critical)
            mess_r.setText("Cannot Running Program!")
            mess_r.exec_()
            
        
def main():
    # Instagram-Downloader v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Instagram-Downloader")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
