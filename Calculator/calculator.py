#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys
width = 401
height = 398
class Window(QWidget):
    result = 0
    def __init__(self):
        super(Window,self).__init__()
        loadUi("calculator.ui",self)
        self.setWindowTitle("ماشین حساب")
        self.setGeometry(500,400,width,height)
        self.setFixedSize(width,height)

            
        self._plus.clicked.connect(self.plus)
        self._manfi.clicked.connect(self.manfi)
        self._zarb.clicked.connect(self.zarb)
        self._tagh.clicked.connect(self.taghsim)
        
        self._0.clicked.connect(self.action_0)
        self._1.clicked.connect(self.action_1)
        self._2.clicked.connect(self.action_2)
        self._3.clicked.connect(self.action_3)
        self._4.clicked.connect(self.action_4)
        self._5.clicked.connect(self.action_5)
        self._6.clicked.connect(self.action_6)
        self._7.clicked.connect(self.action_7)
        self._8.clicked.connect(self.action_8)
        self._9.clicked.connect(self.action_9)
        
        self._result.clicked.connect(self.result)
        self.clear.clicked.connect(self.clear_text)

    def result(self):
        text = self.line.text()
        print(text)
        try:
            text_result = eval(text)
            print(text_result)
            self.line.setText(str(text_result))
        except (Exception):
            self.error_message()
    def plus(self):
        text = self.line.text()
        self.line.setText(text + " + ")

    def manfi(self):
        text = self.line.text()
        self.line.setText(text + " - ")
        
    def zarb(self):
        text = self.line.text()
        self.line.setText(text + " * ")

    def taghsim(self):
        text = self.line.text()
        self.line.setText(text + " / ")

    def action_0(self):
        text = self.line.text()
        self.line.setText(text + "0")
     
    def action_1(self):
        text = self.line.text()
        self.line.setText(text + "1")
     
    def action_2(self):
        text = self.line.text()
        self.line.setText(text + "2")
     
    def action_3(self):
        text = self.line.text()
        self.line.setText(text + "3")

    def action_4(self):
        text = self.line.text()
        self.line.setText(text + "4")
     
    def action_5(self):
        text = self.line.text()
        self.line.setText(text + "5")
     
    def action_6(self):
        text = self.line.text()
        self.line.setText(text + "6")
     
    def action_7(self):
        text = self.line.text()
        self.line.setText(text + "7")
     
    def action_8(self):
        text = self.line.text()
        self.line.setText(text + "8")
     
    def action_9(self):
        text = self.line.text()
        self.line.setText(text + "9")
     
        
    def clear_text(self):
        self.line.clear()
        
    def error_message(self):
        mess = QMessageBox(self)
        mess.setWindowTitle("Error")
        mess.setText("Calculator Error")
        mess.setDetailedText("Calculator Error")
        mess.setStandardButtons(QMessageBox.Ok)
        res = mess.exec_()
        
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("ماشین حساب")
    app.setApplicationDisplayName("Calculator")
    app.setApplicationVersion("1.0")
    
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Calculator v1.0
    main()
    
