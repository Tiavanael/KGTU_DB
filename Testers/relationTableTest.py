from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QItemDelegate
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QListView
from PyQt5.QtWidgets import QTableView

DB_PATH = "../DataBase/cwork.db"
DB_CONNECT = "notebook"

class DateTimeDelegate(QItemDelegate):

    def paint(self, QPainter, QStyleOptionViewItem, QModelIndex):
        length = len(QModelIndex.data(Qt.DisplayRole))
        if length > 1:
            datetime = QDateTime.fromString(QModelIndex.data(Qt.DisplayRole), "hh.mm.ss; dd.MM.yyyy").toPyDateTime()
            string = str(datetime)
        else:
            string = "Неверная дата и время"
        QPainter.drawText(QStyleOptionViewItem.rect, Qt.AlignCenter, string)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        widget = QLineEdit(QWidget)
        return widget


if __name__ == "__main__":

    app = QApplication([])

    QSqlDatabase.addDatabase("QSQLITE", DB_CONNECT)
    QSqlDatabase.database(DB_CONNECT).setDatabaseName(DB_PATH)

    print(QSqlDatabase.database(DB_CONNECT).open())

    model = QSqlRelationalTableModel(db = QSqlDatabase.database(DB_CONNECT))
    model.setTable("notes")
    # model.setJoinMode(QSqlRelationalTableModel.InnerJoin)
    # model.setFilter("work_name like '%ла%'")
    # model.setRelation(1, QSqlRelation("employees", "employee_name", "employee_name"))
    # model.beginInsertColumns(None,2,2)
    # model.insertColumn(2)
    # model.endInsertColumns()
    # model.setRelation(2, QSqlRelation("employees", "employee_name", "salary"))

    model.select()



    view = QListView()
    view.setModel(model)
    view.setItemDelegateForColumn(0, DateTimeDelegate())
    view.show()



    app.exec()

