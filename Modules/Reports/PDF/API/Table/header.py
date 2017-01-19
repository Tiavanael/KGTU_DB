from Modules.Reports.PDF.API.Table.base_row import BaseRow
from Modules.Reports.PDF.API.Table.cell import Cell

from parameters import HEADER_FONT_SIZE



SCALE = 3.78


class Header(BaseRow):

    #INIT
    def __init__(
            self,
            primary_x=0,
            primary_y=0,
            height=40
    ):
        super(Header, self).__init__(
            primary_x = primary_x,
            primary_y = primary_y,
            height = height * SCALE
        )

        # PARMS------------------------------------------

        self._font.setBold(True)
        self._font.setPointSize(HEADER_FONT_SIZE)


    def addCell(self, text, width, font=None):
        if width:
            resizeble = False
            w = width * SCALE
        else:
            w = 30 * SCALE
            resizeble = True

        if self._cells:
            last_cell = self._cells[len(self._cells) - 1]
            x = last_cell.edgeX()
        else:
            x = self._primary_x * SCALE

        cell = Cell(
            x=x,
            y=self._primary_y,
            width=w,
            height=self._height,
            resizeble=resizeble
        )

        if font: cell.setFont(font)
        else: cell.setFont(self._font)

        cell.setText(text)
        self._cells.append(cell)









if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget
    from PyQt5.QtGui import QPainter
    from PyQt5.QtCore import Qt

    class Widget(QWidget):

        # INIT
        def __init__(self):
            super(QWidget, self).__init__()

            self.setFixedSize(800, 500)
            self.header = Header()

            self.header.addCell('headefdsfsdfsdfr_0')
            self.header.addCell('header_1', 150)
            self.header.addCell('header_2')
            self.header.addCell('he')
            self.header.addCell('header_4')

        def paintEvent(self, event):
            p = QPainter()
            p.begin(self)

            p.setFont(self.header.font)
            for cell in self.header.cells:
                p.drawRect(cell)
                p.drawText(cell.textRect(), Qt.AlignCenter, cell.name())

            p.end()




    app = QApplication([])
    win = Widget()
    win.show()
    app.exec_()