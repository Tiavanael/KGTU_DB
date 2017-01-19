from Modules.Reports.PDF.API.Table.base_row import BaseRow
from Modules.Reports.PDF.API.Table.cell import Cell

from parameters import FONT_SIZE






class Row(BaseRow):

    #INIT
    def __init__(
            self,
            parent_row,
            height=60,
            values=[]
    ):
        super(Row, self).__init__(
            height = height,
            primary_x= parent_row.primaryX,
            primary_y= parent_row.edgeY
        )

        self.__values = values



        # PARMS------------------------------------------

        self._font.setBold(False)
        self._font.setPointSize(FONT_SIZE)

        num = 0
        for cell in parent_row.cells:
            self.__addCell(
                text=self.__values[num],
                width=cell.width()
            )
            num += 1


    def __addCell(self, text, width):
        if self._cells:
            last_cell = self._cells[len(self._cells) - 1]
            x = last_cell.edgeX()
        else:
            x = self._primary_x

        cell = Cell(
            x=x,
            y=self._primary_y,
            width=width,
            height=self._height,
            resizeble=False
        )

        cell.setFont(self._font)

        cell.setText(text)

        self._cells.append(cell)









if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget
    from PyQt5.QtGui import QPainter
    from PyQt5.QtCore import Qt
    from Modules.Reports.PDF.API.Table.header import Header


    class Widget(QWidget):

        # INIT
        def __init__(self):
            super(QWidget, self).__init__()

            self.setFixedSize(800, 500)
            self.header = Header()

            self.header.addCell('Сраногорск')
            self.header.addCell('Сранолюдск')
            self.header.addCell('Жопоебск')
            self.header.addCell('Ебложуйск')
            self.header.addCell('Мухосранск')

            self.row = Row(self.header, 30, ['1200 км', '1500 км', '800 км', '1000 км', '2000 км'])
            self.row2 = Row(self.row, 30, ['12', '15', '8', '10', '20'])

        def paintEvent(self, event):
            p = QPainter()
            p.begin(self)

            p.setFont(self.header.font)
            for cell in self.header.cells:
                p.drawRect(cell)
                p.drawText(cell.textRect(), Qt.AlignCenter, cell.name())

            p.setFont(self.row.font)
            for cell in self.row.cells:
                p.drawRect(cell)
                p.drawText(cell.textRect(), Qt.AlignCenter, cell.name())

            for cell in self.row2.cells:
                p.drawRect(cell)
                p.drawText(cell.textRect(), Qt.AlignCenter, cell.name())

            p.end()




    app = QApplication([])
    win = Widget()
    win.show()
    app.exec_()