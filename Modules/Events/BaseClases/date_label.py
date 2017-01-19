from Widgets.Label import MYLabel
from PyQt5.QtCore import QDate





class DateLabel(MYLabel):

    def __init__(self, parent=None):
        super(DateLabel, self).__init__(
            italic=True,
            parent=parent
        )
        self.__date = QDate()

    def setDate(self, qdate):
        self.__date = qdate
        self.setText(self.__date.toString())

    @property
    def date(self): return self.__date
