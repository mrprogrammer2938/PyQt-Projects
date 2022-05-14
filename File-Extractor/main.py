#!/usr/bin/python3
# Zip Extractor v1.0

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import zipfile
import sys

class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/page.ui",self)
        self.setWindowTitle("Zip Extractor")
        self.setWindowIcon(QIcon("./icon/zip-file-icon.png"))
        self.setFixedSize(531,431)
        menu = QMenuBar(self)
        menu.setStyleSheet("color: #fff;")
        about_menu = menu.addMenu("Help")
        help_action = QAction("Help",self)
        help_action.triggered.connect(self.help)
        about_app_action = QAction("About App",self)
        about_app_action.triggered.connect(self.about)
        feedback_action = QAction("Send Feedback",self)
        feedback_action.triggered.connect(self.feedback)
        about_menu.addActions([help_action,about_app_action])
        about_menu.addSeparator()
        about_menu.addAction(feedback_action)
        
        self.choose_file.clicked.connect(self.choose_file_explorer)
        self.choose_file_2.clicked.connect(self.chooser_file_explorer_2)

        self.extract_btn.clicked.connect(self.extract_file)
        self.exit_btn.clicked.connect(self.close)
        
    def extract_file(self):
        try:
            with zipfile.ZipFile(self.zip_file_path.text(),"r") as zip_ref:
                zip_ref.extractall(self.extract_file_path.text())
                mess_i = QMessageBox(self)
                mess_i.setWindowTitle("Extract-File/Information")
                mess_i.setText("File Extracted!")
                mess_i.setDetailedText(f"File Extract On: {self.extract_file_path.text()}")
                mess_i.exec_()
                self.zip_file_path.clear()
                self.extract_file_path.clear()
        except (Exception,):
            mess_r = QMessageBox(self)
            mess_r.setWindowTitle("Extract-File/Error")
            mess_r.setText("Error: Cannot Extract File")
            mess_r.exec_()
    def choose_file_explorer(self):
        file = QFileDialog().getOpenFileName(self,"Open Zip File","C:\\","Zip File (*.zip)")
        if (file != ""):
            self.zip_file_path.setText(file[0])
            
    def chooser_file_explorer_2(self):
        # file = QFileDialog().getSaveFileName(self,"Select Extract Path","C:\\")
        file = QFileDialog().getExistingDirectory(self,"Select Extract File","C:\\")
        if (file != ""):
            self.extract_file_path.setText(file)

    def help(self):
        # Code
        pass
    
    
    def about(self):
        mess_i = QMessageBox(self)
        mess_i.setStyleSheet("color: #fff;")
        mess_i.setWindowTitle("Extract-File/About")
        mess_i.setText("Extract File App v1.0")
        mess_i.exec_()
    
    def feedback(self):
        # Code
        pass
        
        
def main():
    # Extract File App v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Zip Extractor")
    window = Window()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
