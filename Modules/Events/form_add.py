

from Modules.Events.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog
from PyQt5.QtCore import QDate, QTime, QDateTime
from Utility.messages import MESSAGE








class FormAdd(MYDialog):

    def __init__(self, DB, parent=None):
        super(FormAdd, self).__init__(
            parent=parent,
            title='Добавление дела',
        )
        self.attribs = BaseUIAttribs(DB, BaseUIAttribs.Editable, self)
        self.main_layout.addWidget(self.attribs)


    def accept(self):
        current_date = QDate().currentDate()
        current_time = QTime().currentTime()
        current_datetime = QDateTime()
        current_datetime.setDate(current_date)
        current_datetime.setTime(current_time)

        if self.attribs.dataStructure.qDateTime > current_datetime:
            super(FormAdd, self).accept()
        else:
            MESSAGE.error(
                title='Поздняя дата',
                text='Выбраная дата/время уже в прошлом. Пожалуйста выберите другую дату/время'
            )








if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormAdd()
    win.show()
    app.exec_()

