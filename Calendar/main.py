#!/usr/bin/python3
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("form.ui",self)
        self.setWindowTitle("تقویم")
        self.calendar.selectionChanged.connect(self.change_date)
        
    def change_date(self):
        date = self.calendar.selectedDate()
        self.label.setText(f"تاریخ:  {str(date.toPyDate())}")
        
        
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
