
#Qt Types
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime

from DataBase.datetime_converter import DateTimeConverter


class Structure(object):
    """
    Данный класс хранит структуру данных
    для работы со "Встречей".

    Property:
            FIO: <str> : ФИО
          place: <str> : место встречи
          state: <bool> : состояние встречи
          qDate: <QDate> : Qt дата
          qTime: <QTime> : Qt время
        strTime: <str>: время в виде строки
        strDate: <str>: дата в виде строки
      qDateTime: <QDateTime>: Qt времядата
     dbDateTime: <DBDateTime>: БД времядата
    task: <str> :  описание встречи
    """


    def __init__(
            self,
            fio=None,
            place=None,
            descript=None,
            qdate_qtime=None,
            q_time=None,
            q_datetime=None,
            db_datetime=None,
            state=None
    ):
        """
        Для определения даты и времени возможно
        указать один из следущих параметров:
            - qdate_qtime
            - q_datetime
            - db_datetime
        Параметры написаны в приорететном порядке
        (т.е. после qdate_qtime параметры q_datetime
        и db_datetime использоваться не будут).


        :param fio: <str> : ФИО
        :param place: <str> : место встречи
        :param descript: <str> : описание дела
        :param qdate_qtime: <tuple(QDate, QTime)> : Qt дата и Qt время
        :param q_datetime: <QDateTime> : Qt время и дата
        :param db_datetime: <DBDateTime> : БД время и дата
        """

        self.__init_Attributes()
        self.__init_Parameters(
            fio=fio ,
            place=place,
            descript=descript,
            state=state,
            qdate_qtime=qdate_qtime,
            q_time=q_time,
            q_datetime=q_datetime,
            db_datetime=db_datetime
        )




    # inits
    def __init_Attributes(self):
        super(Structure, self).__init__()

        self.__fio = ''
        self.__place = ''
        self.__descript = ''
        self.__state = 0
        self.__datetime = QDateTime()
        self.__db_datetime = ''

    def __init_Parameters(self, fio, place, descript, state, qdate_qtime, q_time, q_datetime, db_datetime):
        if fio: self.setFIO(fio)
        if place: self.setPlace(place)
        if descript: self.setDescription(descript)
        if state: self.setState(state)
        if qdate_qtime: self.setDate(qdate_qtime[0], qdate_qtime[1])
        else:
            if q_datetime:
                self.setQDateTime(q_datetime)
            else:
                if db_datetime:
                    self.setDBDateTime(db_datetime)


    

    # PROPERTY
    @property
    def FIO(self):
        try:
            return self.__fio
        except:
            return None

    @property
    def place(self):
        try:
            return self.__place
        except:
            return None

    @property
    def description(self):
        try:
            return self.__descript
        except:
            return None

    @property
    def state(self):
        try:
            return self.__state
        except:
            return None

    @property
    def qDate(self):
        try:
            return self.__datetime.date()
        except:
            return None

    @property
    def qTime(self):
        try:
            return self.__datetime.time()
        except:
            return None

    @property
    def strDate(self):
        try:
            return self.__datetime.date().toString()
        except:
            return None

    @property
    def strTime(self):
        try:
            return self.__datetime.time().toString()[0:5]
        except:
            return None

    @property
    def qDateTime(self):
        try:
            return self.__datetime
        except:
            return None

    @property
    def dbDateTime(self):
        try:
            return self.__db_datetime
        except:
            return None

    @property
    def asFieldsForRecord(self):
        """
        Список значений для таблицы БД
        :return: list
        """
        vals = [
            self.FIO,
            self.place,
            self.dbDateTime,
            self.description,
            self.state
        ]
        return vals



    # METHODS
    def setFIO(self, FIO='Фамилия Имя Отчество'):
        FIO = str(FIO)
        self.__fio = FIO

    def setPlace(self, place):
        """
        :param place: <str> : место встречи
        """

        place = str(place)
        self.__place = place

    def setDescription(self, text=''):
        text = str(text)
        self.__descript = text

    def setState(self, state=0):
        self.__state = state

    def setDate(self, qdate, qtime):
        """
        :param qdate: <QDate>
        :param qtime: <QTime>
        """

        self.__datetime.setDate(qdate)
        self.__datetime.setTime(qtime)
        self.__db_datetime = DateTimeConverter.qtToDb(self, self.__datetime)

    def setQDateTime(self, qdatetime):
        self.__datetime = qdatetime
        self.__db_datetime = DateTimeConverter.qtToDb(self, self.__datetime)

    def setDBDateTime(self, db_datetime):
        self.__db_datetime = db_datetime
        self.__datetime = DateTimeConverter.dbToQt(self, self.__db_datetime)







if __name__ == '__main__':
    date = QDate()
    time = QTime()

    date.setDate(2012, 7, 10)
    time.setHMS(13, 45, 0)

    fio = 'Курлыкин Иван Иваныч'
    role = 'Собеседование'
    descript = 'Встреча в метрополисе'

    struct = Structure(
        fio=fio,
        place=role,
        descript=descript,
        #qdate_qtime=(date, time)
        db_datetime='2016-09-08 20:30:00'
    )


    print(struct.dbDateTime)
