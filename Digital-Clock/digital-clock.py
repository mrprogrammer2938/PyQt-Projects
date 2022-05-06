#!/usr/bin/python3
# Digital Clock
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Clock(QWidget):
    
    def __init__(self):
        super(Clock,self).__init__()
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("./icon/clock-icon.png"))
        self.setGeometry(500,100,400,100)
        self.setFixedSize(400,100)
        self.setStyleSheet("""
QWidget {
   background-color: #111;
}
QLabel {
   color: #90ee90;
}
        """)
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.label.setFont(QFont("Arial",55))
        layout.addWidget(self.label)
        timer = QTimer(self)
        timer.timeout.connect(self.set_time)
        timer.start(1000)
        self.setLayout(layout)
        
    def set_time(self):
        current_time = QTime().currentTime()
        time_zone = current_time.toString("hh:mm:ss")
        self.label.setText(time_zone)
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Digital Clock")
    app.setApplicationVersion("v1.0")
    clock = Clock()
    clock.show()
    app.exec_()
if __name__ == "__main__":
    main()
