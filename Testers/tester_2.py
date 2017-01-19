
from Modules.Reports.PDF.main import ReportFile, Header, ReportTable

from Widgets.Widget import MYWidget
from Widgets.PushButton import MYPushButton



class ReportWidget(MYPushButton):

    #INIT
    def __init__(self):
        super(ReportWidget, self).__init__()


        # ATTRIBUTES-------------------------------------

        self.report_file  = ReportFile()
        self.report_table = ReportTable()
        self.table_header = Header(0, 0, 30)

        # END ATTRIBUTES---------------------------------




        # PARMS------------------------------------------

        self.setText('Create PDF')

        self.table_header.addCell('Сраногорск_1', width=40)
        self.table_header.addCell('Сраногорск_2', width=40)
        self.table_header.addCell('Сраногорск_3', width=40)
        self.table_header.addCell('Сраногорск_4', width=40)
        self.table_header.addCell('Сраногорск_5', width=40)

        self.report_table.setHeader(self.table_header)

        self.report_table.addRow(['1', '2', '3', '4', '5'])
        self.report_table.addRow(['1', '2', '3', '4', '5'])
        self.report_table.addRow(['1', '2', '3', '4', '5'])
        self.report_table.addRow(['1', '2', '3', '4', '5'])
        self.report_table.addRow(['1', '2', '3', '4', '5'])
        self.report_table.addRow(['1', '2', '3', '4', '5'])

        self.report_file.setFilePath("test.pdf")
        self.report_file.setTable(self.report_table)

        # END PARMS--------------------------------------




        self.clicked.connect(self.report_file.create)
        self.clicked.connect(self.openCreatedFile)

    def openCreatedFile(self):
        import os
        # окрывает созданный файл
        os.system("test.pdf")







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = ReportWidget()
    win.show()
    app.exec_()