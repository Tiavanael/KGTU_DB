from Modules.Reports.PDF.API.Table.cell import QFont






class BaseRow(object):

    #INIT
    def __init__(
            self,
            primary_x,
            primary_y,
            height
    ):
        super(BaseRow, self).__init__()


        # ATTRIBUTES-------------------------------------

        self._height = height
        self._font   = QFont()
        self._cells  = []
        self._primary_x = primary_x
        self._primary_y = primary_y
        self._edge_x = None
        self._edge_y = self._primary_y + height




    #PROPERTY--------------------------------------------

    @property
    def font(self): return self._font

    @property
    def height(self): return self._height

    @property
    def edgeX(self): return self._edge_x

    @property
    def edgeY(self): return self._edge_y

    @property
    def primaryX(self): return self._primary_x

    @property
    def primaryY(self): return self._primary_y

    @property
    def cells(self): return tuple(self._cells)




    # METHODS--------------------------------------------

    def setHeight(self, height):
        if height > 9: self._height = height


    def setFont(self, qfont):
        self._font = qfont


    def setPrimaryX(self, x):
        if x >= 0: self._primary_x = x


    def setPrimaryY(self, y):
        if y >= 0: self._primary_y = y










if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget
    from PyQt5.QtGui import QPainter
    from PyQt5.QtCore import Qt

    class Widget(QWidget):

        # INIT
        def __init__(self):
            super(QWidget, self).__init__()

            self.setFixedSize(800, 500)
            self.baserow = BaseRow(50, 50, 60)

            print('cells  = ', self.baserow.cells)
            print('edgeX  = ', self.baserow.edgeX)
            print('edgeY  = ', self.baserow.edgeY)
            print('font   = ', self.baserow.font)
            print('height = ', self.baserow.height)
            print('primX  = ', self.baserow.primaryX)
            print('primY  = ', self.baserow.primaryY)

        def paintEvent(self, event):
            p = QPainter()
            p.begin(self)


            p.end()




    app = QApplication([])
    win = Widget()
    win.show()
    app.exec_()