from PyQt5.QtCore import QDateTime, QDate, QTime
from DataBase.datetime_converter import DateTimeConverter





class Structure(object):
    """
    Данный класс хранит структуру данных
    для работы с "Заметками" (Notes).

    Property:
          theme: <str> : тема заметки
    task: <str> : описание заметки
          qDate: <QDate> : Qt дата
          qTime: <QTime> : Qt время
        strTime: <str>: время в виде строки
        strDate: <str>: дата в виде строки
      qDateTime: <QDateTime>: Qt времядата
     dbDateTime: <DBDateTime>: БД времядата
    """


    def __init__(
            self,
            theme=None,
            description=None,
            q_datetime=None,
            qdate_qtime=None,
            db_datetime=None
    ):

        self.__init_Attributes()
        self.__init_Parameters(
            theme=theme,
            description=description,
            qdate_qtime=qdate_qtime,
            q_datetime=q_datetime,
            db_datetime=db_datetime
        )




    # inits
    def __init_Attributes(self):
        super(Structure, self).__init__()
        self.__theme = ''
        self.__description = ''
        self.__q_datetime = QDateTime()
        self.__db_datetime = ''

    def __init_Parameters(self, theme, description, q_datetime, qdate_qtime, db_datetime):
        if theme: self.setTheme(theme)
        if description: self.setDescription(description)
        if qdate_qtime: self.setDate(qdate_qtime[0], qdate_qtime[1])
        else:
            if q_datetime:
                self.setQDateTime(q_datetime)
            else:
                if db_datetime:
                    self.setDBDateTime(db_datetime)


    

    @property
    def asFieldsForRecord(self):
        return [
            self.__theme,
            self.__description,
            self.__db_datetime
        ]
    
    @property
    def theme(self):
        try:
            return self.__theme
        except:
            return None

    @property
    def description(self):
        try:
            return self.__description
        except:
            return None

    @property
    def qDate(self):
        try:
            return self.__q_datetime.date()
        except:
            return None

    @property
    def qTime(self):
        try:
            return self.__q_datetime.time()
        except:
            return None

    @property
    def strDate(self):
        try:
            return self.__q_datetime.date().toString()
        except:
            return None

    @property
    def strTime(self):
        try:
            return self.__q_datetime.time().toString()[0:5]
        except:
            return None

    @property
    def qDateTime(self):
        try:
            return self.__q_datetime
        except:
            return None

    @property
    def dbDateTime(self):
        try:
            return self.__db_datetime
        except:
            return None




    # METHODS
    def setTheme(self, theme=''):
        theme = str(theme)
        self.__theme = theme

    def setDescription(self, descript=''):
        self.__description = str(descript)

    def setDate(self, qdate, qtime):
        """
        :param qdate: <QDate>
        :param qtime: <QTime>
        """

        self.__q_datetime.setDate(qdate)
        self.__q_datetime.setTime(qtime)
        self.__db_datetime = DateTimeConverter.qtToDb(self, self.__q_datetime)

    def setQDateTime(self, qdatetime):
        self.__q_datetime = qdatetime
        self.__db_datetime = DateTimeConverter.qtToDb(self, self.__q_datetime)

    def setDBDateTime(self, db_datetime):
        self.__db_datetime = db_datetime
        self.__q_datetime = DateTimeConverter.dbToQt(self, self.__db_datetime)











if __name__ == '__main__':
    d = QDate(2012, 10, 10)
    t = QTime(22, 50)

    dt = QDateTime()
    dt.setDate(d)
    dt.setTime(t)

    theme = 'Тема'
    desc = 'Описание'

    s = Structure(
        theme=theme,
        description=desc,
        qdate_qtime=(d, t)
    )

    print(s.asFieldsForRecord)
    print(s.qDate)
    print(s.qTime)
    print(s.strDate)
    print(s.strTime)



