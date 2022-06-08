#!/usr/bin/python3
# Calendar v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        global date
        self.setWindowTitle("Calendar")
        self.setGeometry(500,100,500,400)
        self.setFixedSize(500,400)
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(50,30)
        cal.clicked[QDate].connect(self.show_date)
        self.lbl = QLabel(self)
        self.lbl.setFont(QFont("Arial",18))
        self.lbl.setGeometry(145,255,400,100)
        # self.lbl.move(170,300)
        date = cal.selectedDate()
        self.lbl.setText(date.toString("yyyy:MM:dd"))
    
    def show_date(self,date):
        self.lbl.setText(date.toString())
        
        
def main():
    # Calendar v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Calendar")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
