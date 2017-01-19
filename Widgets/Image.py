from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QImage
import os


class MYImage(QWidget):

    def __init__(self, img_path=None, parent=None):
        super(MYImage, self).__init__()

        self.__init_Attributes()
        self.__init_Parameters(img_path, parent)



    #inits
    def __init_Attributes(self):
        self.__height = 128
        self.__width  = 128
        self.__image  = QImage()
        self.__path   = ''

    def __init_Parameters(self, img_path, parent):
        self.setImagePath(img_path)
        if parent: self.setParent(parent)


    #EVENTS
    def paintEvent(self, event):
        painter = QPainter()
        rect = event.rect()
        painter.begin(self)
        painter.setRenderHint(painter.HighQualityAntialiasing)
        painter.drawImage(rect, self.__image)
        painter.end()




    # PROPERTY
    def imagePath(self): return self.__path



    # METHODS
    def setImagePath(self, path):
        try:
            if os.path.exists(path):
                self.__path = path
                self.__image = QImage(self.__path)
        except:
            pass



if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = MYImage(img_path='C:/Users/Edward/Desktop/Develop/Projects/CGPM/Resources/Icons/Dialogs/error.png')
    win.show()
    sys.exit(app.exec_())
