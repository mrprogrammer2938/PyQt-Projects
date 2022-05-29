#!/usr/bin/python3
# Pdf Reader v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        global title_
        title_ = "PDF Reader"
        self.setWindowTitle(title_)
        self.setWindowIcon(QIcon("./icon/pdf-reader-icon.png"))
        self.setGeometry(500,70,1000,800)
        menu = QMenuBar(self)
        self.setMenuWidget(menu)
        filemenu = menu.addMenu("File")
        open_file_action = QAction("Open File",self)
        open_file_action.setWhatsThis("Open File")
        open_file_action.setStatusTip("Open File")
        open_file_action.setShortcut("Ctrl+o")
        open_file_action.triggered.connect(self.open_file)
        exit_action = QAction("Exit",self)
        exit_action.setWhatsThis("Exit")
        exit_action.setStatusTip("Exit")
        exit_action.setShortcut("Alt+f4")
        exit_action.triggered.connect(self.close)
        filemenu.addAction(open_file_action)
        filemenu.addSeparator()
        filemenu.addAction(exit_action)
        
        self.webView = QWebEngineView(self)
        self.webView.settings().setAttribute(QWebEngineSettings.PluginsEnabled,True)
        self.webView.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled,True)
        self.setCentralWidget(self.webView)
        
    def open_file(self):
        global file_
        try:
            file_ = QFileDialog().getOpenFileName(self,"Open PDF File","C:\\","All Files (*.*);;PDF File (.pdf)")
            self.webView.setUrl(QUrl(file_[0]))
            title_ = f"PDF Reader - {file_[0]}"
            self.setWindowTitle(title_)
        except (Exception,) as err:
            print(err)
        
def main():
    # PDF Reader v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("PDF-Reader")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
