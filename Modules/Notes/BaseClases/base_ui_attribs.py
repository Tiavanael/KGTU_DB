# Qt Types

from Modules.Notes.BaseClases.data_structure import Structure
from Modules.Notes.BaseClases.date_label import DateLabel
from Modules.Notes.BaseClases.time_label import TimeLabel


# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout

from Widgets.DateEdit import MYDateEdit
from Widgets.LineEdit import MYLineEdit
from Widgets.Label import MYLabel
from Widgets.TimeEdit import MYTimeEdit
from Widgets.Widget import MYWidget
from PyQt5.QtWidgets import QTextEdit, QTextBrowser







class BaseUIAttribs(MYWidget):
    """
    Базовый класс, обеспечивающий GUI
    для атрибутов "Контакта".
    """

    # роль
    Editable = 0
    NotEditable = 1

    def __init__(self, role=Editable, parent=None):
        """
        Параметр role должен принимать одно из
        двух значений:
            - Editable    - редактируемый GUI
            - NotEditable - не редактируемый GUI

        :param role: <BaseUIAttribs.Editable, BaseUIAttribs.NotEditable>
        :param parent: <QtWidget> : Qt родитель
        """



        super(BaseUIAttribs, self).__init__(
            parent=parent,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=10
        )

        self.__uitype = role
        self.__structure = Structure()

        if self.__uitype == self.Editable:
            self.__init_EditableAttributes()
        else:
            self.__init_NotEditableAttributes()

        self.__init_Parameters()
        self.__init_Layouting()




    # inits
    def __init_EditableAttributes(self):
        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_theme    = MYLabel(parent=self, bold=True, text='Тема:')
        self.__lbl_date = MYLabel(parent=self, bold=True, text='Дата:')
        self.__lbl_time = MYLabel(parent=self, bold=True, text='Время:')

        self.__theme   = MYLineEdit(parent=self)
        self.__descript = QTextEdit(self)
        self.__date = MYDateEdit(self)
        self.__time = MYTimeEdit(self)

    def __init_NotEditableAttributes(self):
        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_theme = MYLabel(parent=self, bold=True, text='Тема:')
        self.__lbl_date = MYLabel(parent=self, bold=True, text='Дата:')
        self.__lbl_time = MYLabel(parent=self, bold=True, text='Время:')

        self.__theme = MYLabel(parent=self, bold=False, text='')
        self.__descript = QTextBrowser(self)
        self.__date = DateLabel(parent=self)
        self.__time = TimeLabel(parent=self)

    def __init_Parameters(self):
        if self.__uitype == self.Editable:
            self.__date.setCalendarPopup(True)
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addWidget(self.__descript)
        self.main_layout.addLayout(self.btns_layout)

        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_theme)
        self.__form_layout.setWidget(1, AS_LABEL, self.__lbl_date)
        self.__form_layout.setWidget(2, AS_LABEL, self.__lbl_time)

        self.__form_layout.setWidget(0, AS_FIELD, self.__theme)
        self.__form_layout.setWidget(1, AS_FIELD, self.__date)
        self.__form_layout.setWidget(2, AS_FIELD, self.__time)





    @property
    def dataStructure(self):
        theme = self.__theme.text()
        descript = self.__descript.toPlainText()

        if self.__uitype == self.Editable:
            date = self.__date.date()
            time = self.__time.time()
        else:
            date = self.__date.date
            time = self.__time.time

        self.__structure.setTheme(theme)
        self.__structure.setDate(date, time)
        self.__structure.setDescription(descript)

        return self.__structure


    # METHODS
    def setDataStructure(self, struct):
        self.__structure = struct

        self.__theme.setText(struct.theme)
        self.__descript.setText(struct.description)
        self.__date.setDate(struct.qDate)
        self.__time.setTime(struct.qTime)










if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QDateTime, QDate, QTime
    app = QApplication([])

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


    win = BaseUIAttribs(BaseUIAttribs.Editable)
    win.setDataStructure(s)

    win.show()
    app.exec_()



