from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication

from DataBase.access_model import DBAccessModel
from Utility.ReportClass import Report
from paths import DB_FILE_PATH

app = QApplication([])
rep = Report(name="Тестовый отчет")
db = QSqlDatabase('QSQLITE')
db.setDatabaseName("../DataBase/app_data_base.db")
if db.open():
    model = DBAccessModel(table="events", app_db=db)
    model.select()
    rep.addTableFromModel(model)
    rep.showPreview()
    app.exec()
