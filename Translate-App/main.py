#!/usr/bin/python3
# Translator App v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

import sys,googletrans  

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/page.ui",self)
        self.setWindowTitle("Translator App")
        self.setWindowIcon(QIcon("./icon/translate-icon.png"))
        
        self.exit_action.setShortcut("Alt+f4")
        self.exit_action.setWhatsThis("Exit")
        self.exit_action.setStatusTip("Exit")
        self.exit_action.triggered.connect(self.close)
        
        self.help_action.triggered.connect(self.help)
        self.about_action.triggered.connect(self.about)
        self.feedback_action.triggered.connect(self.feedback)
        
        self.clear_btn.clicked.connect(self.clear_all_txt)
        self.translate_btn.clicked.connect(self.translate)
        
        self.statusBar().addWidget(QLabel("Translate App v1.0",self))
        
        self.add_language()
    def add_language(self):
        for lang in googletrans.LANGUAGES.values():
            self.combo.addItem(lang.capitalize())
            self.combo_2.addItem(lang.capitalize())
            
        self.combo.setCurrentText("Persian")
        self.combo_2.setCurrentText("English")
    def translate(self):
        self.text = self.txt.toPlainText()
        self.fromlang = self.combo.currentText()
        self.tolang = self.combo_2.currentText()
        translator = googletrans.Translator()
        translate_ = translator.translate(self.text,src=self.fromlang,dest=self.tolang)
        self.txt2.setText(translate_.text)
    
    def clear_all_txt(self):
        self.txt.clear()
        self.txt2.clear()
    
    def help(self):
        pass
    
    def about(self):
        pass 
    
    def feedback(self):
        pass

def main():
    # Translator App v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Translator App")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
