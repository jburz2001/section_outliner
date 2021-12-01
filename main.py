import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    
    xpos, ypos, w, h = 100, 100, 600, 400
    win.setGeometry(xpos,ypos,w,h)
    win.setWindowTitle("I am a window")
    
    win.show()
    sys.exit(app.exec_())
    
window()