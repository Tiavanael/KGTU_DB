from collections import OrderedDict
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import QDateTime








class DBAccessModel(QSqlTableModel):

    # table names
    TableContacts = 'contacts'
    TableDepartments = 'departments'
    TableEmployees = 'employees'
    TableEmployeesTask = 'employees_task'
    TableEvents = 'events'
    TableNotes = 'notes'
    TableTasks = 'tasks'
    TableDepartmentTasks = 'department_task'


    # record type
    SqlRecord = 0
    DictRecord = 1
    PyDictRecord = 2




    def __init__(self, table, app_db, parent=None):
        """
        :param table: <DBAccessModel.TableName> : имя таблицы из неймспейса данного класса
        :param app_db: <QSqlDataBase> : подключенная к приложению БД
        """

        super(DBAccessModel, self).__init__(parent, app_db)

        self.setEditStrategy(self.OnRowChange)
        self.setTable(table)


    # METHODS
    def addRecord(self, fields, row=0):
        """
        Добавление записи в таблицу
        :param row: место вставки; по умолчанию вставляет в начало
        :param fields: массив значений атрибутов записи
        """

        record = self.record(0)
        record.clearValues()
        i = 0
        for value in fields:
            record.setValue(i, str(value))
            i += 1
        self.insertRecord(row, record)
        self.select()

    def removeRecord(self, row=-1):
        """
        Удаление записи под номером "row";
        по умолчанию удаляет последнюю запись
        :param row: номер записи
        """

        if row < 0:
            row = self.rowCount() - 1
        self.removeRow(row)
        self.select()

    def getRecord(self, row=0, record_type=DictRecord):
        """
        Получение записи
        :param row:
        :param table:
        :param record_type:
            SqlRecord    - получение QSqlRecord
            DictRecord   - получение упорядоченного словаря
            PyDictRecord - получение питоновского словаря
        """

        record = self.record(row)

        if record_type == self.SqlRecord:
            return record
        elif record_type == self.DictRecord:
            cols = record.count()
            dict = OrderedDict()
            for i in range(0, cols):
                dict[record.field(i).name()] = record.value(i)
            return dict
        elif record_type == self.PyDictRecord:
            cols = record.count()
            dict = {}
            for i in range(0, cols):
                dict[record.field(i).name()] = record.value(i)
            return dict

    def editRecord(self, row=0, fields = []):
        record = self.record(row)
        i = 0
        for item in fields:
            record.setValue(i, str(item))
            i += 1
        self.setRecord(row, record)
        self.select()
        return record

    def setTable(self, table):
        super(DBAccessModel, self).setTable(table)
        self.select()

    def setHeaders(self, headers=[]):
        for i in range(0, len(headers)):
            self.setHeaderData(i, 1, str(headers[i]))

    def setDateTimeFilter(self, compare_sign, field ="datetime", type = "dt", date = QDateTime().currentDateTime()):
        """
        :param compare_sign: <str> : Логическая операция сравнения с датой date
        [==, >, >=, <, <=]
        :param date: Дата для сравнения, По умолчанию текущая
        """
        if type == "dt" :
            self.setFilter(
                "datetime(" + field + ") "
                + compare_sign
                + " datetime('"
                + str(date.toPyDateTime()) + "')"
            )
        elif type == "d":
            self.setFilter(
                "date(" + field + ") "
                + compare_sign
                + " date('"
                + str(date.toPyDateTime()) + "')"
            )

    def setPoisk(self, field, text):
        self.setFilter(field +" like('%" + text +"%')")
        self.select()







