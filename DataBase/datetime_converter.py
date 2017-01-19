from PyQt5.QtCore import QDateTime

class DateTimeConverter(object):
    """
    Данный класс позволяет конвертировать
    данные в формат для БД.
    То есть перед занесением данных в БД они
    должны пройти конвертацию !!!
    """
    def __init__(self):

        self.__init_Attributes()
        

    #inits
    def __init_Attributes(self):
        super(DateTimeConverter, self).__init__()
    





    # конверторы В БД формат
    def qtToDb(self, q_datetime):
        """
        Конвертирует Qt дату в дату для БД
        :param q_date: <QDateTime> : Qt дата
        """
        return str(q_datetime.toPyDateTime())[:16]


    # конверторы ИЗ БД формата
    def dbToQt(self, db_date):
        """
        Конвертирует дату БД в Qt дату
        :param db_date: <BD_DateType> : дата из БД
        """
        pattern = "yyyy-MM-dd hh:mm"
        return QDateTime().fromString(db_date, pattern)






from PyQt5.QtCore import QDateTime, QDate, QTime
#
# d = QDate(2014, 10 ,10)
# t = QTime(22, 30)
# dt = QDateTime()
# dt.setDate(d)
# dt.setTime(t)
# db = TypeConverter().QDateTimeToDbDateTime(dt)

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QTimeEdit
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    t = QTime(22, 30)
    win = QTimeEdit()
    win.setTime(t.currentTime())

    d = QDate(2014, 10, 10)
    t = win.time()
    dt = QDateTime()
    dt.setDate(d)
    dt.setTime(t)
    print(dt.toPyDateTime())
    db = DateTimeConverter().qtToDb(dt)
    print(db)
    # win.show()
    sys.exit(app.exec_())