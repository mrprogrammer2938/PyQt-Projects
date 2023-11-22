# pip install PyQt5
# pip install pyshorteners

from PyQt5.QtWidgets import *
from form import Ui_MainWindow
import sys
from pyshorteners import Shortener

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("URL Shortener")
        
        self.ui.make_btn.clicked.connect(self.make_shortlink)
        self.ui.copy_btn.clicked.connect(self.copy_link)
        
    def make_shortlink(self):
        url = self.ui.url.text()
        short_ = Shortener().osdb
        url_short = short_.short(url)
        self.ui.text.setText(url_short)
    def copy_link(self):
        self.ui.text.selectAll()
        self.ui.text.copy()    
def main():
    app = QApplication(sys.argv)
    app.setApplicationVersion("1")
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
