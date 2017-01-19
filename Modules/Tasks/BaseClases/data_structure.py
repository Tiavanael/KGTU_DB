# Qt Types
from PyQt5.QtCore import QDate
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime

from DataBase.datetime_converter import DateTimeConverter


class Structure(object):
    def __init__(self):


        self.__init_Attributes()


    # inits
    def __init_Attributes(self):
        super(Structure, self).__init__()

        self.__name = ''
        self.__task = ''
        self.__datetime_start = ''
        self.__datetime_finish = QDateTime()
        self.__db_datetime_start = QDateTime()
        self.__db_datetime_finish = ''
        self.__state = 0

    # PROPERTY
    @property
    def name(self):
        try:
            return self.__name
        except:
            return None

    @property
    def task(self):
        try:
            return self.__task
        except:
            return None

    @property
    def qDateStart(self):
        try:
            return self.__datetime_start.date()
        except:
            return None

    @property
    def qTimeStart(self):
        try:
            return self.__datetime_start.time()
        except:
            return None

    @property
    def strDateStart(self):
        try:
            return self.__datetime_start.date().toString()
        except:
            return None

    @property
    def strTimeStart(self):
        try:
            return self.__datetime_start.time().toString()[0:5]
        except:
            return None

    @property
    def qDateTimeStart(self):
        try:
            return self.__datetime_start
        except:
            return None

    @property
    def dbDateTimeStart(self):
        try:
            return self.__db_datetime_start
        except:
            return None

    @property
    def qDateFinish(self):
        try:
            return self.__datetime_finish.date()
        except:
            return None

    @property
    def qTimeFinish(self):
        try:
            return self.__datetime_finish.time()
        except:
            return None

    @property
    def strDateFinish(self):
        try:
            return self.__datetime_finish.date().toString()
        except:
            return None

    @property
    def strTimeFinish(self):
        try:
            return self.__datetime_finish.time().toString()[0:5]
        except:
            return None

    @property
    def qDateTimeFinish(self):
        try:
            return self.__datetime_finish
        except:
            return None

    @property
    def dbDateTimeFinish(self):
        try:
            return self.__db_datetime_finish
        except:
            return None

    @property
    def state(self):
        return self.__state

    @property
    def asFieldsForRecord(self):
        vals = [
            self.name,
            self.task,
            self.dbDateTimeStart,
            self.dbDateTimeFinish,
            self.state
        ]
        return vals




    # METHODS
    def setName(self, name):
        name = str(name)
        self.__name = name

    def setTask(self, task):

        task = str(task)
        self.__task = task

    def setDateStart(self, qdate, qtime):
        self.__datetime_start.setDate(qdate)
        self.__datetime_start.setTime(qtime)
        self.__db_datetime_start = DateTimeConverter().qtToDb(self.__datetime_start)

    def setQDateTimeStart(self, qdatetime):
        self.__datetime_start = qdatetime
        self.__db_datetime_start = DateTimeConverter().qtToDb(self.__datetime_start)

    def setDBDateTimeStart(self, db_datetime):
        self.__db_datetime_start = db_datetime
        self.__datetime_start = DateTimeConverter().dbToQt(self.__db_datetime_start)

    def setDateFinish(self, qdate, qtime):
        self.__datetime_finish.setDate(qdate)
        self.__datetime_finish.setTime(qtime)
        self.__db_datetime_finish = DateTimeConverter().qtToDb(self.__datetime_finish)

    def setQDateTimeFinish(self, qdatetime):
        self.__datetime_finish = qdatetime
        self.__db_datetime_finish = DateTimeConverter().qtToDb(self.__datetime_finish)

    def setDBDateTimeFinish(self, db_datetime):
        self.__db_datetime_finish = db_datetime
        self.__datetime_finish = DateTimeConverter().dbToQt(self.__db_datetime_finish)

    def setState(self, state):
        self.__state = state

    def clear(self):
        self.__name = ''
        self.__task = ''
        self.__datetime_start  = QDateTime()
        self.__datetime_finish = QDateTime()
        self.__db_datetime_start  = ''
        self.__db_datetime_finish = ''





if __name__ == '__main__':
    date = QDate()
    time = QTime()

    date.setDate(2012, 7, 10)
    time.setHMS(13, 45, 0)

    fio = 'Курлыкин Иван Иваныч'
    role = 'Собеседование'
    descript = 'Встреча в метрополисе'

    struct = Structure()

    print(struct.dbDateTime)
