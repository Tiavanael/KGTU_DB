# Qt Types

from Modules.Events.BaseClases.data_structure import Structure
from Modules.Events.BaseClases.date_label import DateLabel
from Modules.Events.BaseClases.time_label import TimeLabel
from DataBase.access_model import DBAccessModel

# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QTextEdit
from Widgets.TimeEdit import MYTimeEdit
from Widgets.DateEdit import MYDateEdit
from Widgets.LineEdit import MYLineEdit
from Widgets.ComboBox import MYComboBox
from Widgets.Label import MYLabel
from Widgets.Widget import MYWidget
from Widgets.CheckBox import MYChekBox
from PyQt5.QtCore import Qt, QTime, QDate, QDateTime




class BaseUIAttribs(MYWidget):
    """
    Базовый класс, обеспечивающий GUI
    для атрибутов "Контакта".
    """

    # роль
    Editable = 0
    NotEditable = 1

    def __init__(self, DB, role=Editable, parent=None):
        super(BaseUIAttribs, self).__init__(
            parent=parent,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=10
        )

        self.__init_Attributes(role, DB)
        self.__init_Parameters()
        self.__init_Layouting()




    # inits
    def __init_Attributes(self, role, DB):
        self.__structure = Structure()

        self.__uitype = role

        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_fio   = MYLabel(parent=self, bold=True, text='ФИО:')
        self.__lbl_time  = MYLabel(parent=self, bold=True, text='Время:')
        self.__lbl_date  = MYLabel(parent=self, bold=True, text='Дата:')
        self.__lbl_place = MYLabel(parent=self, bold=True, text='Место:')
        self.__lbl_state = MYLabel(parent=self, bold=True, text='Состояние:')

        if self.__uitype == self.Editable:
            self.__fio_model = DBAccessModel(table=DBAccessModel.TableContacts, app_db=DB)
            self.__time  = MYTimeEdit(self)
            self.__date  = MYDateEdit(self)
            self.__place  = MYLineEdit(parent=self)
            self.__fio   = MYComboBox(parent=self)
            self.__descript = QTextEdit(self)
            self.__state = MYChekBox(parent=self)
        else:
            self.__time = TimeLabel(parent=self)
            self.__date = DateLabel(parent=self)
            self.__place = MYLabel(parent=self, italic=True, text='')
            self.__fio  = MYLabel(parent=self, italic=True, text='')
            self.__descript = QTextBrowser(self)
            self.__state = MYLabel(parent=self, italic=True, text='')

    def __init_Parameters(self):
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

        if self.__uitype == self.Editable:
            current_time = QTime.currentTime()
            current_time.setHMS(
                current_time.hour(),
                current_time.minute(),
                current_time.second()
            )
            self.__state.setCheckable(True)
            self.__date.setCalendarPopup(True)
            self.__date.setDate(QDate.currentDate())
            self.__time.setTime(current_time)
            self.__fio.setModel(self.__fio_model)

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addWidget(self.__descript)
        self.main_layout.addLayout(self.btns_layout)

        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_fio)
        self.__form_layout.setWidget(1, AS_LABEL, self.__lbl_date)
        self.__form_layout.setWidget(2, AS_LABEL, self.__lbl_time)
        self.__form_layout.setWidget(3, AS_LABEL, self.__lbl_place)
        self.__form_layout.setWidget(4, AS_LABEL, self.__lbl_state)

        self.__form_layout.setWidget(0, AS_FIELD, self.__fio)
        self.__form_layout.setWidget(1, AS_FIELD, self.__date)
        self.__form_layout.setWidget(2, AS_FIELD, self.__time)
        self.__form_layout.setWidget(3, AS_FIELD, self.__place)
        self.__form_layout.setWidget(4, AS_FIELD, self.__state)




    # class tools
    def __tool_SetFIO(self, FIO):
        FIO = str(FIO)
        self.__structure.setFIO(FIO)
        if self.__uitype == self.Editable:
            self.__fio.setCurrentText(FIO)
        else:
            self.__fio.setText(FIO)

    def __tool_SetPlace(self, place):
        """
        :param place: <str> : назначение дела
        """

        place = str(place)
        self.__structure.setPlace(place)
        self.__place.setText(place)

    def __tool_SetDescription(self, text=''):
        text = str(text)
        self.__structure.setDescription(text)
        self.__descript.setText(text)

    def __tool_SetState(self, state):
        # print(state)
        self.__structure.setState(state)

        if self.__uitype == self.Editable:
            if state == 1:
                self.__state.setCheckState(Qt.Checked)
            else:
                self.__state.setCheckState(Qt.Unchecked)
        else:
            if state == 1:
                self.__state.setText('Выполнено')
            else:
                self.__state.setText('Не выполнено')

    def __tool_SetDateTime(self, q_datetime):
        self.__structure.setQDateTime(q_datetime)
        self.__time.setTime(self.__structure.qTime)
        self.__date.setDate(self.__structure.qDate)

    def __tool_SetDBDateTime(self, db_datetime):
        self.__structure.setDBDateTime(db_datetime)
        self.__time.setTime(self.__structure.qTime)
        self.__date.setDate(self.__structure.qDate)





    @property
    def dataStructure(self):
        place = self.__place.text()
        descript = self.__descript.toPlainText()

        if self.__uitype == self.Editable:
            FIO = self.__fio.currentText()
            date = self.__date.date()
            time = self.__time.time()
            if self.__state.isChecked(): state = 1
            else: state = 0
        else:
            FIO = self.__fio.text()
            date = self.__date.date
            time = self.__time.time
            if self.__state.text() == 'Выполнено': state = 1
            else: state = 0

        self.__structure.setFIO(FIO)
        self.__structure.setDate(date, time)
        self.__structure.setDescription(descript)
        self.__structure.setPlace(place)
        self.__structure.setState(state )

        return self.__structure


    # METHODS
    def setDataStructure(self, struct):
        self.__tool_SetFIO(struct.FIO)
        self.__tool_SetPlace(struct.place)
        self.__tool_SetDescription(struct.description)
        self.__tool_SetDateTime(struct.qDateTime)
        self.__tool_SetState(struct.state)

    def updateModel(self):
        self.__fio_model.select()






if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    from PyQt5.QtCore import QDate, QTime
    date = QDate()
    time = QTime()

    date.setDate(2012, 7, 10)
    time.setHMS(13, 45, 0)

    fio = 'Курлыкин Иван Иваныч'
    role = '8911488943'
    descript = 'Встреча в метрополисе'


    struct = Structure(
        fio=fio,
        place=role,
        descript=descript,
        qdate_qtime=(date, time)
    )

    win = BaseUIAttribs()
    win.setDataStructure(struct)

    win.show()
    app.exec_()

