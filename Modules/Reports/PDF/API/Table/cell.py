

from PyQt5.QtGui  import QFont, QFontMetrics
from PyQt5.QtCore import QRect, QMargins






class Cell(QRect):

    #INIT
    def __init__(
            self,
            x=50,
            y=50,
            width=50,
            height=30,
            text='cell',
            resizeble=True
    ):
        super(Cell, self).__init__(x, y, width, height)




        # ATTRIBUTES-------------------------------------

        self.__text = text
        self.__font = QFont()
        self.__text_metrics = QFontMetrics(self.__font)
        self.__resizeble = resizeble
        self.__margins = QMargins(5, 5, 5, 5)


        # PARMS------------------------------------------

        if self.__resizeble: self.__resizeX()




    # PROPERTIES------------------------------------------

    def text(self): return self.__text

    def font(self): return self.__font

    def edgeX(self): return self.x() + self.width()

    def edgeY(self): return self.y() + self.height()

    def margins(self): return self.__margins

    def resizeble(self): return self.__resizeble

    def textRect(self):
        return QRect(
            self.x() + self.__margins.left(),
            self.y() + self.__margins.top(),
            self.width() - self.__margins.left() - self.__margins.right(),
            self.height() - self.__margins.top() - self.__margins.bottom()
    )




    # METHODS--------------------------------------------

    def __textWidth(self):
        return self.__text_metrics.width(self.__text)


    def __textHeight(self):
        return self.__text_metrics.height()


    def __resizeX(self):
        # width of zone for name
        accept_w  = self.width() - self.__margins.left() - self.__margins.right()

        text_w = self.__textWidth()

        if accept_w < text_w:
            delta_w = text_w - accept_w
            self.setWidth(self.width() + delta_w)


    def __resizeY(self):
        # height of zone for name
        accept_h = self.height() - self.__margins.top() - self.__margins.bottom()

        text_h = self.__textHeight()

        if accept_h < text_h:
            delta_h = text_h - accept_h
            self.setHeight(self.height() + delta_h)


    def setText(self, text):
        self.__text = text
        if self.__resizeble: self.__resizeX()


    def setFont(self, qfont):
        self.__font = qfont
        self.__text_metrics = QFontMetrics(self.__font)
        if self.__resizeble: self.__resizeX()


    def setMargins(self, l, t, r, b):
        self.__margins.setLeft(l)
        self.__margins.setTop(t)
        self.__margins.setRight(r)
        self.__margins.setBottom(b)
        if self.__resizeble: self.__resizeX()


    def setResizeble(self, state=True):
        self.__resizeble = state














if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget
    from PyQt5.QtGui import QPainter
    from PyQt5.QtCore import Qt

    class Widget(QWidget):

        # INIT
        def __init__(self):
            super(QWidget, self).__init__()

            self.setFixedSize(800, 500)
            self.cell = Cell()

        def paintEvent(self, event):
            p = QPainter()
            p.begin(self)

            p.setFont(self.cell.font())
            p.drawRect(self.cell)
            p.drawText(self.cell.textRect(), Qt.AlignCenter, self.cell.text())

            p.end()




    app = QApplication([])
    win = Widget()
    win.show()
    app.exec_()






