#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from googletrans import Translator
import pyjokes
import sys
width = 502
height = 414


class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("file3.ui",self)
        self.setWindowTitle("جک")
        self.setGeometry(500,400,width,height)
        self.setFixedSize(width,height)
        
        self.btn.clicked.connect(self.joke)
        self.clear_btn.clicked.connect(self.clear_joke)
        
    def joke(self):
        joke = pyjokes.get_joke()
        translator = Translator()
        translate = translator.translate(joke,src="en",dest="fa ")
        self.text.setText(translate.text)
    
    def clear_joke(self):
        self.text.clear()
        
        
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("جک")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Joke v1.0
    main()
    
