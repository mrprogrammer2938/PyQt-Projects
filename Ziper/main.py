#!/usr/bin/python3
#

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from form import Ui_MainWindow
import shutil
import qdarkstyle
import sys,os,time

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setupUi(self)
        style = qdarkstyle.load_stylesheet_pyqt5()
        self.setStyleSheet(style)
        self.setWindowTitle("Ziper")
        self.move(500,100)
        self.start_btn.clicked.connect(self.make_zip)
        self.choose_folder_btn.clicked.connect(self.choose_folder)
        
    # def set_combo(self):
    #     text = self.combo.currentIndex()
    #     if text == 0:
    #         self.start_btn.clicked.disconnect(self.choose_zip)
    #         self.start_btn.clicked.connect(self.choose_folder)
    #         self.zip_form()

    #     elif text == 1:
    #         self.start_btn.clicked.disconnect(self.choose_folder)
    #         self.start_btn.clicked.connect(self.choose_zip)
    #         self.unzip_form()
    # def zip_form(self):
    #     self.label.setText("Enter Folder: ")
    #     self.line.setPlaceholderText("Folder Path...")
    #     self.choose_folder_btn.setText("Choose Folder")
    #     self.choose_folder_btn.clicked.connect(self.choose_folder)
    #     self.start_btn.clicked.connect(self.make_zip)
    # def unzip_form(self):
    #     self.label.setText("Enter Zip: ")
    #     self.line.setPlaceholderText("Enter Zip...")
    #     self.choose_folder_btn.setText("Choose Zip")
    #     self.choose_folder_btn.clicked.connect(self.choose_zip)
    #     self.start_btn.clicked.connect(self.make_unzip)
    #     self.start_btn.setText("Unzip")
    def choose_folder(self):
        self.folder = QFileDialog().getExistingDirectory(self,"Select Folder","C:\\")
        self.line.setText(self.folder)
        if self.folder != "":
            for item in os.listdir(self.folder):
                self.folder_list.addItem(item)
        else:
            return
    # def choose_zip(self):
    #     self.zipfile_ = QFileDialog().getOpenFileName(self,"Open Zip","C:\\","Zip File (*.zip)")
    #     print(self.zipfile_)
    #     self.line.setText(self.zipfile_[0])
        
        #self.folder_list.addItem()
        
    def make_zip(self):
        try:
            self.folder_path = self.line.text()
            zipfile = shutil.make_archive(self.folder_path,"zip",self.folder_path)
            time.sleep(1)
            self.show_finishmessage()
        except Exception as err:
            QMessageBox.information(self,title="Error",message=err)
            
    # def make_unzip(self):
    #     try:
    #         self.folder_path = self.line.text()
    #         zipfile = shutil.unpack_archive(self.folder_path,"output")
    #         time.sleep(1)
    #         self.show_finishmessage()
    #     except Exception as err:
    #         QMessageBox.information(self,title="Error",message=err)
    def show_finishmessage(self):
        mess = QMessageBox(self)
        mess.setText("Completed!")
        mess.setIcon(QMessageBox.Information)
        
        mess.show()    
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Ziper")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    
