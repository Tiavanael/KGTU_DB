
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt



class TablePainter(QPainter):

        # INIT
        def __init__(self, canvas):
            super(TablePainter, self).__init__(canvas)

        def drawTable(self, table):


            #header drawing
            self.setFont(table.header().font)
            for cell in table.header().cells:
                self.drawRect(cell)
                self.drawText(cell.textRect(), Qt.AlignCenter, cell.name())

            #rows drawing
            self.setFont(table.rowsFont())
            for row in table.rows():
                for cell in row.cells:
                    self.drawRect(cell)
                    self.drawText(cell.textRect(), Qt.AlignCenter, cell.name())

