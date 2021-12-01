import cv2 as cv

class Ui():
    def __init__(self, path):
        self.path_ = path
    
    def print(self):
        print(self.path_)

ui = Ui("hello")
ui.print()