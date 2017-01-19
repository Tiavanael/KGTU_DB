from PyQt5.QtWidgets import QLabel

from Widgets.Widget import MYWidget


class About(MYWidget):
    def __init__(self):
        super(About, self).__init__()
        self.__label = QLabel('Агафонов Олег Игоревич.\n Группа 14-ВТ', self)
        self.main_layout.addWidget(self.__label)
        self.main_layout.addItem(self.main_spacer)
