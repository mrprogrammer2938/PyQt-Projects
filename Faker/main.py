#!/usr/bin/python3
# Faker v1.0

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
from faker import Faker
import sys
fake = Faker()
class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/page.ui",self)
        self.setWindowTitle("Faker")
        self.setWindowIcon(QIcon("./icon/fake-icon.png"))
        self.setFixedSize(400,489)
        self.make_btn.clicked.connect(self.make_fake_profile)
        self.txt.setReadOnly(1)
    def make_fake_profile(self):
        fake_profile = f"""Name: {fake.name()}
Email: {fake.email()}
Address: {fake.address()}
Country: {fake.country()}
"""
        self.txt.setText(fake_profile)
    
    
def main():
    # Faker v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Faker")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
