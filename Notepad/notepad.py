from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Notepad(QMainWindow):
    def __init__(self):
        super(Notepad,self).__init__()
        self.y = False
        self.file_name = "Untitled"
        self.setWindowTitle(f"Notepad - {self.file_name}")
        self.setWindowIcon(QIcon("./icon/notepad-icon.png"))
        self.setGeometry(450,100,850,600)
        
        self.txt = QTextEdit(self)
        self.txt.setFont(QFont("Arial",10))
        self.setCentralWidget(self.txt)
        m = QMenuBar(self)
        self.setMenuBar(m)
        file_menu = m.addMenu("File")
        view_menu = m.addMenu("View")
        edit_menu = m.addMenu("Edit")
        help_menu = m.addMenu("Help")
        new_file_action = QAction("New File",self)
        new_file_action.setShortcut("Ctrl+n")
        new_file_action.triggered.connect(self.new_file)
        open_file_action = QAction("Open File",self)
        open_file_action.setShortcut("Ctrl+o")
        open_file_action.triggered.connect(self.open_file)
        save_file_action = QAction("Save",self)
        save_file_action.setShortcut("Ctrl+s")
        save_file_action.triggered.connect(self.save_file)
        save_as_file_action = QAction("Save As",self)
        save_as_file_action.setShortcut("Ctrl+Shift+s")
        save_as_file_action.triggered.connect(self.save_as_file)
        exit_action_action = QAction("Exit",self)
        exit_action_action.setShortcut("Alt+F4")
        exit_action_action.triggered.connect(self.close)
        
        file_menu.addActions([new_file_action,open_file_action,save_file_action,save_as_file_action])
        file_menu.addSeparator()
        file_menu.addAction(exit_action_action)
        
        normal_action = QAction("Normal",self)
        normal_action.triggered.connect(lambda: self.showNormal())
        fullscreen_action = QAction("FullScreen",self)
        fullscreen_action.triggered.connect(lambda: self.showFullScreen())
        minimize_action = QAction("Minimize",self)
        minimize_action.triggered.connect(lambda: self.showMinimized())
        font_action = QAction("Select Font",self)
        font_action.triggered.connect(self.select_font)
        view_menu.addActions([normal_action,fullscreen_action,minimize_action])
        view_menu.addSeparator()
        view_menu.addAction(font_action)
        undo_action = QAction("Undo",self)
        undo_action.setShortcut("Ctrl+z")
        undo_action.triggered.connect(lambda: self.txt.undo())
        redo_action = QAction("Redo",self)
        redo_action.setShortcut("Ctrl+y")
        redo_action.triggered.connect(lambda: self.txt.redo())
        cut_action = QAction("Cut",self)
        cut_action.setShortcut("Ctrl+x")
        cut_action.triggered.connect(lambda: self.txt.cut())
        copy_action = QAction("Copy",self)
        copy_action.setShortcut("Ctrl+c")
        copy_action.triggered.connect(lambda: self.txt.copy())
        paste_action = QAction("Paste",self)
        paste_action.setShortcut("Ctrl+v")
        paste_action.triggered.connect(lambda: self.txt.paste())
        delete_action = QAction("Delete",self)
        delete_action.setShortcut("Delete")
        delete_action.triggered.connect(lambda: self.txt.clear())
        select_all_action = QAction("Select All",self)
        select_all_action.setShortcut("Ctrl+a")
        select_all_action.triggered.connect(lambda: self.txt.selectAll())
        
        edit_menu.addActions([undo_action,redo_action])
        edit_menu.addSeparator()
        edit_menu.addActions([cut_action,copy_action,paste_action])
        edit_menu.addSeparator()
        edit_menu.addAction(delete_action)
        edit_menu.addSeparator()
        edit_menu.addAction(select_all_action)
        help_action = QAction("Help",self)
        help_action.triggered.connect(self.help_app)
        about_action = QAction("About Notepad",self)
        about_action.triggered.connect(self.about)
        feedback_action = QAction("Send Feedback",self)
        feedback_action.triggered.connect(self.feedback)
        help_menu.addActions([help_action,about_action])
        help_menu.addSeparator()
        help_menu.addAction(feedback_action)
    def new_file(self):
        self.file_name = "Untitled"
        self.txt.clear()
        self.setWindowTitle(f"Notepad - {self.file_name}")
        self.file = ""
        self.y = False
        
    def open_file(self):
        self.file = QFileDialog.getOpenFileName(self,"Open File","C:\\","All Files (*.*)")
        file_ = open(self.file[0],"r").read()
        self.txt.setText(file_)
        self.y = True
        self.file_name = self.file[0]
        self.setWindowTitle(f"Notepad - {self.file_name}")

    def save_file(self):
        if (self.y==False):
            try:
                self.file = QFileDialog.getSaveFileName(self,"Save File","C:\\","All Files (*.*)")
                file_ = open(self.file[0],"w")
                file_.write(self.txt.toPlainText())
                file_.close()
                self.y = True
                self.file_name = self.file[0]
                self.setWindowTitle(f"Notepad - {self.file_name}")
            except (Exception,):
                pass
        elif (self.y==True):
            file_ = open(self.file[0],"w")
            file_.write(self.txt.toPlainText())
            file_.close()
    def save_as_file(self):
        try:
            self.file = ""
            self.file = QFileDialog.getSaveFileName(self,"Save As","C:\\","All Files (*.*)")
            file_ = open(self.file[0],"w")
            file_.write(self.txt.toPlainText())
            file_.close()
            self.y = True
            self.file_name = self.file[0]
            self.setWindowTitle(f"Notepad - {self.file_name}")
        except (Exception,):
            pass
            
    
    def select_font(self):
        (font_,ok) = QFontDialog.getFont(QFont("Arial",10),self)
        if ok:
            self.txt.setFont(font_)
        else:
            pass
    
    def help_app(self):
        pass
    
    def about(self):
        mess = QMessageBox(self)
        mess.setWindowTitle("About Notepad")
        mess.setText("Notepad v1.0")
        mess.setDetailedText("Hello")
        mess.exec_()

    def feedback(self):
        pass
    
def main():
    # Notepad v1.0
    app = QApplication(sys.argv)
    app.setApplicationName("Notepad")
    app.setApplicationVersion("v1.0")
    app.setWindowIcon(QIcon("./icon/notepad-icon"))
    notepad = Notepad()
    notepad.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
