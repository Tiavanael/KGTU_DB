import sys

from PyQt5.QtCore import QDate
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QItemDelegate

from paths import DB_FILE_PATH

class Record():

    def __init__(self, theme, text, datetime):

        self.theme = theme
        self.text = text
        self.datetime = datetime

class Model(QSqlTableModel):

    def __init__(self, db):
        super(QSqlTableModel, self).__init__(db = db)

        self.queue = []

class Application(QApplication):

    def __init__(self, args = []):
        super(QApplication, self).__init__(args)
        import Testers.notes
        self.window = Testers.notes.getForm()
        self.timer = QTimer()

    def setDataView(self):

        self.currentDateTime = QDateTime()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(DB_FILE_PATH)
        if self.db.open():
            print("База данных подключена!")

            self.model = Model(db = self.db)
            self.model.setTable("notes")
            self.model.setHeaderData(0, 1, "Время")
            self.model.setHeaderData(1, 1, "Тема")
            self.model.setHeaderData(2, 1, "Выполнение")
            self.model.setEditStrategy(self.model.OnRowChange)
            self.model.select()

            self.window.noteList.setModel(self.model)
            self.window.noteList.setColumnWidth(0, 70)
            self.window.noteList.hideColumn(3)
            self.window.noteList.setItemDelegate(noteListDelegate(self.window.noteList))

            self.window.calendar.clicked.connect(self.selectCalendarDate)
            self.window.noteList.clicked.connect(self.selectNote)

            self.window.addNoteButton.clicked.connect(self.addNote)
            self.window.remNoteButton.clicked.connect(self.remNote)
            self.window.saveButton.clicked.connect(self.saveNote)

            self.window.calendar.setSelectedDate(QDate())
            self.selectCalendarDate()

        else:
            print("База данных не подключена, ошибка!")

    def selectCalendarDate(self):
        date = self.window.calendar.selectedDate()
        self.currentDateTime.setDate(date)
        self.window.dateTimeEdit.__tool_SetDateTime(self.currentDateTime)
        self.model.setFilter("date(datetime) == date('" + str(date.toPyDate()) + "')")

    def selectNote(self):
        rowNumb = self.window.noteList.selectedIndexes()[0].row()
        self.window.noteList.selectRow(rowNumb)
        self.currentDateTime = QDateTime.fromString(
            self.model.index(rowNumb, 0).data(Qt.DisplayRole)[0:16],
            "yyyy-MM-dd hh:mm"
        )
        self.window.dateTimeEdit.__tool_SetDateTime(self.currentDateTime)
        self.showNoteItems(
            self.model.record(rowNumb).value(1),
            self.model.record(rowNumb).value(3)
        )

    def addNote(self):
        self.selectCalendarDate()
        row = self.model.record(0)
        self.currentDateTime.setTime(QTime.currentTime())
        row.setValue(0, str(self.currentDateTime.toPyDateTime())[0:23])
        row.setValue(1, "")
        row.setValue(2, 0)
        row.setValue(3, "")
        rc = self.model.rowCount()
        self.model.insertRecord(rc, row)

    def remNote(self):

        rows = self.window.noteList.selectedIndexes()
        if rows:
            for item in rows:
                self.model.removeRow(item.row())
            self.selectCalendarDate()

    def saveNote(self):
        rows = self.window.noteList.selectedIndexes()
        if rows:
            rowNumb = rows[0].row()
            row = self.model.record(rowNumb)
            print()
            row.setValue(0, str(self.window.dateTimeEdit.dateTime().toPyDateTime()))
            row.setValue(1, self.window.themeEdit.name())
            # row.setValue(2, 0)
            row.setValue(3, self.window.textEdit.toPlainText())
            print(row.value(3))
            self.model.setRecord(rowNumb, row)

    def showNoteItems(self, theme, text):

        self.window.themeEdit.setName(theme)
        self.window.textEdit.setName(text)

    def start(self):

        self.setDataView()

        self.window.show()
        self.timer.start(1000)

        sys.exit(self.exec_())

class noteListDelegate(QItemDelegate ):

    def __init__(self, ListView):
        super(QItemDelegate, self).__init__()
        self.ListView = ListView

    def paint(self, Painter, StyleOptionViewItem, ModelIndex):
        try:
            if self.ListView.selecterIndexes()[0].row() == ModelIndex.row():
                Painter.setColor(Qt.red)
                Painter.drawRect(StyleOptionViewItem.rect)
        except: pass
        text = ""
        col = ModelIndex.column()
        str = ModelIndex.data(Qt.DisplayRole)
        if col == 2:
            if str == 0:
                text = "Не выполено"
            elif str == 1:
                text = "В процессе"
            elif str == 2:
                text = "Выполнено"
        elif col == 0:
            datetimeText = ""
            if len(str) > 0:
                datetimeText = QDateTime.fromString(
                    str[0:16],
                    "yyyy-MM-dd HH:mm"
                ).time().toString()[0:5]

            text = datetimeText
        elif col == 1:
            text = str
        Painter.drawText(StyleOptionViewItem.rect, Qt.AlignCenter, text)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        pass













