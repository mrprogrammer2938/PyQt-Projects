#!/usr/bin/python3
# QrCode Maker v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys
import qrcode
import webbrowser

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/page.ui",self)
        self.setWindowTitle("QrCode Maker")
        self.setWindowIcon(QIcon("./icon/qrcode-icon.png"))
        self.setFixedSize(400,300)
        menu = QMenuBar(self)
        menu.setStyleSheet("color: #fff;")
        option_menu = menu.addMenu("Options")
        about_action = QAction("About",self)
        about_action.triggered.connect(self.about)
        feedback_action = QAction("Send Feedback",self)
        feedback_action.triggered.connect(self.feedback)
        exit_action = QAction("Exit",self)
        exit_action.setShortcut("Alt+f4")
        exit_action.triggered.connect(self.close)
        help_action = QAction("Help",self)
        help_action.setShortcut("Ctrl+h")
        help_action.triggered.connect(self.help)
        instagram_action = QAction("Instagram",self)
        instagram_action.triggered.connect(self.instagram)
        help_menu = option_menu.addMenu("Help")
        help_menu.addAction(instagram_action)
        help_menu.addSeparator()
        help_menu.addAction(help_action)
        help_menu.addAction(about_action)
        help_menu.addSeparator()
        help_menu.addAction(feedback_action)
        option_menu.addSeparator()
        option_menu.addAction(exit_action)
        
        self.make_btn.clicked.connect(self.make_qrcode)
    def make_qrcode(self):
        if self.file_path.text() != "" and self.file_path.text() != " ":
            if self.file_path.text()[-4:] == ".png" or self.file_path.text()[-4:] == ".PNG":
                img = qrcode.make(self.link_inp.text())
                img.save(self.file_path.text(),"PNG")
            else:
                img = qrcode.make(self.link_inp.text())
                img.save(f"{self.file_path.text()}.png","PNG")

    def instagram(self):
        webbrowser.open_new_tab("https://instagram.com/sina.python")

    def feedback(self):
        pass
    
    def about(self):
        mess_i = QMessageBox(self)
        mess_i.setStyleSheet("color: #fff;")
        mess_i.setWindowTitle("QrCode-Maker/Information")
        mess_i.setText("QrCode-Maker v1.0")
        mess_i.exec_()
    def help(self):
        pass  
        
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("QrCode Maker")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
