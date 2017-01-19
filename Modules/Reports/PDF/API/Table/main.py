from Modules.Reports.PDF.API.Table.header import Header
from Modules.Reports.PDF.API.Table.row import Row
from PyQt5.QtGui import QFont







class ReportTable(object):
    
    #INIT
    def __init__(self, header=Header()):
        super(ReportTable, self).__init__()
        

        self.__header = header
        self.__rows_height = 30
        self.__rows_font = QFont()
        self.__rows   = []



    #PROPERTY

    def rowsFont(self):
        return self.__rows_font


    def rows(self):
        return self.__rows


    def header(self): return self.__header


    def row(self, num):
        try:
            return self.__rows[num]
        except:
            return None



    #METHODS

    def addRow(self, val=['val_0', 'val_1', 'val_2']):
        if self.__rows:
            last_row = self.__rows[len(self.__rows) - 1]
        else:
            last_row = self.__header

        row = Row(last_row, self.__rows_height, val)

        self.__rows.append(row)


    def setHeader(self, header=Header()):
        self.__header = header


    def setRowsHeight(self, height):
        if height > 9: self.__rows_height = height


    def setRowsFont(self, qFont):
        """
        arg: qfont = QFont()
        """
        self.__rows_font = qFont










if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget
    from Modules.Reports.PDF.API.Table.painter import TablePainter
    from PyQt5.QtCore import Qt


    class Widget(QWidget):

        # INIT
        def __init__(self):
            super(QWidget, self).__init__()

            self.setFixedSize(800, 500)
            header = Header()
            header.addCell('Сраногорск')
            header.addCell('Сранолюдск')
            header.addCell('Жопоебск')
            header.addCell('Ебложуйск')
            header.addCell('Мухосранск')

            self.table = ReportTable()
            self.table.setHeader(header)
            self.table.addRow(['1200 км', '1500 км', '800 км', '1000 км', '2000 км'])
            self.table.addRow(['', '', '', '', ''])
            self.table.addRow(['', '', '', '', ''])
            self.table.addRow(['', '', '', '', ''])
            self.table.addRow(['', '', '', '', ''])
            self.table.addRow(['', '', '', '', ''])




        def paintEvent(self, event):
            p = TablePainter(self)

            p.begin(self)

            p.drawTable(self.table)

            p.end()




    app = QApplication([])
    win = Widget()
    win.show()
    app.exec_()
