from Widgets.Label import MYLabel
from PyQt5.QtCore import QTime


class TimeLabel(MYLabel):
    def __init__(self, parent=None):
        super(TimeLabel, self).__init__(
            italic=True,
            parent=parent
        )

        self.__time = QTime()

    def setTime(self, qtime):
        self.__time = qtime
        self.setText(self.__time.toString()[:5])

    @property
    def time(self): return self.__time


