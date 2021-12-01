import cv2 as cv

class Ui():
    def __init__(self, path):
        self.path_ = path
        #self.imgs_ = []
        # self.base_img_
    
    def printPath(self):
        print(self.path_)
        
    def showFileFromPath(self,type):
        #type
        #   1=color
        #   0=grayscale
        #   -1=unchanged
        img = cv.imread(self.path_, type)
        cv.imshow("Image",img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    
ui = Ui("assets\afm.png")
ui.showFileFromPath(1)