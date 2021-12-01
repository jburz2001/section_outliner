#https://www.youtube.com/watch?v=-2uyzAqefyE&list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj&index=2

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        x,y,w,h = 200,200,300,300
        self.setGeometry(x,y,w,h)
        winTitle = "Section Outliner"
        self.setWindowTitle(winTitle)
        self.initUi()
        
    def initUi(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("I am label")
        self.label.move(50,50)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed button")
    
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
    
window()