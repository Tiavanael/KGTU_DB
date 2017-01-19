# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:




#PYQT
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

from parameters import ENABLE_STYLES
from parameters import FONT_SIZE
from parameters import HEADER_FONT_SIZE
from style import STYLE




class MYTableWidget(QTableWidget):
    #INIT
    def __init__(self,
                 parent=None,
                 row=0,
                 col=0,
                 headers=[],
                 sortable=True,
                 alt_colors=True,
                 ):

        super(MYTableWidget, self).__init__()

        self.editable = True

        #PARMS
        if parent: self.setParent(parent)
        header_font = QFont()
        header_font.setBold(True)
        header_font.setPointSize(HEADER_FONT_SIZE)

        row_font = QFont()
        row_font.setPointSize(FONT_SIZE)

        self.horizontalHeader().setFont(header_font)
        self.setFont(row_font)

        self.setAlternatingRowColors(alt_colors)
        self.setRowCount(row)

        if headers:
            cols = len(headers)
            self.setColumnCount(cols)
            self.setHorizontalHeaderLabels(headers)
        else:
            self.setColumnCount(col)
            headr = []
            for i in range(col):
                headr.append('col_'+str(i))
            self.setHorizontalHeaderLabels(headr)

        self.setAlternatingRowColors(alt_colors)
        self.setSortingEnabled(sortable)
        self.horizontalHeader().setStretchLastSection(True)

        #STYLING
        if ENABLE_STYLES: self.setStyleSheet(STYLE.TableWidget)

    #METHODES
    def itemRefactor(self, item):
        if self.editable:
            row = item.row()
            text = item.name()
            if (row == 0):
                if text != '':
                    self.insertRow(0)
                    self.setItem(0, 0, QTableWidgetItem(''))
            elif (row != 0):
                if text == '':
                    self.removeRow(row)


    def getColumnList(self, col):
        result = []
        for row in range(self.rowCount()):
            item = self.item(row, col)
            if item:
                if item.name() != '':
                    result.append(item.name())
        return result




if __name__ == '__main__':
    app = QApplication([])
    win = MYTableWidget(row=1,
                        col=1)
    win.itemChanged.connect(win.itemRefactor)
    row = 0

    win.blockSignals(True)
    win.setRowCount(10)
    for i in '0123456789':
        item = QTableWidgetItem(i)
        win.setItem(row, 0, item)
        row += 1
    win.blockSignals(False)
    # win.removeRows([0, 1, 2, 10])
    win.show()
    app.exec_()