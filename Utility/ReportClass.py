from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QTextDocument
from PyQt5.QtGui import QTextTableFormat
from PyQt5.QtPrintSupport import QPrintPreviewDialog, QPrinter, QPrintDialog
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTextEdit


class Report():

    printed = False
    printer = None
    previewDialog = None
    document = None
    FontSize = 8
    Html = ''
    webView = None
    string = ''

    def setString(self, str):
        self.string = str

    def __init__(self, name = 'Отчет', date = QDate.currentDate()):
        self.__initObjects()

        self.name = name
        self.date = date

        # self.document.setDefaultStyleSheet("""
        # table { border: 5}
        # td { spacing: 10}
        # """)
        self.Html += """
        <style type=\"name/css\">
        table {
            border: 5px solid black
        }
        </style>
        """
        self.__setHeader()

    def showPreview(self):
        self.previewDialog = QPrintPreviewDialog(self.printer)
        # self.previewDialog.setMaximumSize(1000,2000)
        # self.previewDialog.setFixedSize(500,700)
        self.previewDialog.paintRequested.connect(self.Print)
        self.previewDialog.exec()
        self.printed = True
        # self.Print()

    def __initObjects(self):
        self.printer = QPrinter(QPrinter.HighResolution)
        #self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setPageSize(QPrinter.A4)

        self.document = QTextDocument()
        self.document.setDefaultFont(QFont("Times",self.FontSize))

    def __setHeader(self):
        self.Html += "\
        <div>\
            <h3 align='center'>" + self.name + "</h3>\
            <h4 align='right'>" + self.date.toString() + "</h4>\
        </div>\
        "

    def addString(self, string = None):
        if string == None:
            self.Html += "<br><h2>" + self.string + "<\h2>"
        else:
            self.Html += string

    def addTable(self,fields, rows):
        self.Html += '<table '
        # self.Html += 'border="2" style=" border-style:solid; border-color:black'
        self.Html += ' cellspacing="0" cellpadding="6" width="100%">'

        self.Html += "<thead><tr>"
        self.Html += "<th width='8%'><strong>№</strong></th>"
        for item in fields:
            self.Html += "<th ><strong>"+str(item)+"</strong></th>"

        self.Html += "</tr></thead>"
        N = 0
        self.Html += "<tbody>"
        for row in rows:
            N += 1
            self.Html += "<tr>"
            self.Html += "<td align='center'>"+str(N)+"</td>"
            for item in row:
                self.Html += "<td"
                self.Html += " padding='5' align='center'>"+str(item)+"</td>"
            self.Html += "</tr>"


        self.Html += "</tbody></table><br>"

    def addTableFromModel(self, model, fieldsIndexes = [], fieldsNames = {}, delegates = {}):
        fields = []

        for i in range(0, model.columnCount()):
            if len(fieldsIndexes) > 0 and i in fieldsIndexes:
                    pass
            else:
                try:
                    fields.append(fieldsNames[i])
                except:
                    fields.append(model.record(0).fieldName(i))

        rows = []
        for i in range(0, model.rowCount()):
            row = []
            for j in range(0, model.columnCount()):
                if len(fieldsIndexes) > 0 and j in fieldsIndexes:
                        pass
                else:
                    try:
                        row.append(delegates[j](model.record(i).value(j)))
                    except:
                        row.append(model.record(i).value(j))
            rows.append(row)

        self.addTable( fields, rows)

    def Print(self):
        self.printer.setFullPage(True)

        self.document.setHtml(self.Html)

        # if not self.printed:
        self.document.print(self.printer)




