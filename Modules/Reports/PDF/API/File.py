# coding: utf-8



from Modules.Reports.PDF.API.Table.painter import TablePainter
from PyQt5.QtPrintSupport import QPrinter
from Utility.errors import ERROR





class ReportFile(object):

    """
    Класс <File> предназначен для создания *.pdf файла.
    Вначале определяются:
        - путь файла "setFilePath('C:/Desktop/myfile.pdf')"
        - таблица (необязательно) "setTable(table=Table())"
         а после генерируется сам файл:
        - "create()".
    """

    def __init__(self):
        super(ReportFile, self).__init__()


        self.__path  = 'C:/'
        self.__table = None


    def filePath(self): return self.__path


    def create(self):
        if self.__path:
            printer = QPrinter()
            #настройки принтера
            printer.setOutputFormat(printer.PdfFormat)
            printer.setPageSize(printer.A4)
            #printer.setFullPage(True)
            printer.setPaperSize(printer.A4)
            printer.setOutputFileName(self.__path)

            painter = TablePainter(printer)
            # всё рисование происходит тут
            # размеры PDF-страницы = A4(210x297)

            #test
            # painter.drawLine(0, 0, 210, 297)
            # painter.drawRect(0, 0, 210, 297)

            #прорисовка таблицы
            if self.__table: painter.drawTable(self.__table)


            painter.end()


        else:
            ERROR.error(
                cls='File',
                mthd='create()',
                msg='Не указан путь для создания файла'
            )


    def setFilePath(self, path):
        """
        arg: path = str()
        """
        self.__path = path


    def setTable(self, table):
        """
        arg: table = Table()
        """
        self.__table = table







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QFont
    from Modules.Reports.PDF.API.Table.main import ReportTable, Header

    app = QApplication([])



    #HEADER
    header = Header(0, 0, 20)
    header.addCell('Сраногорск_1', width=40)
    header.addCell('Сраногорск_2', width=40)
    header.addCell('Сраногорск_3', width=40)
    header.addCell('Сраногорск_4', width=40)
    header.addCell('Сраногорск_5', width=40)



    # TABLE
    font = QFont()
    font.setPointSize(12)

    table = ReportTable()
    table.setRowsFont(font)
    table.setHeader(header)
    table.setRowsHeight(30)

    table.addRow(['1', '2', '3', '4', '5'])
    table.addRow(['1', '2', '3', '4', '5'])
    table.addRow(['1', '2', '3', '4', '5'])
    table.addRow(['1', '2', '3', '4', '5'])
    table.addRow(['1', '2', '3', '4', '5'])
    table.addRow(['1', '2', '3', '4', '5'])



    #FILE
    pdf = ReportFile()

    pdf.setFilePath("C:\\Users\\Edward\\Desktop\\asd.pdf")
    pdf.setTable(table)

    pdf.create()

    import os
    # окрывает созданный файл
    os.system(pdf.filePath())