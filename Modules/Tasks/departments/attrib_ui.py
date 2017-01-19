# Qt Types
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QTextBrowser

from Modules.Tasks.BaseClases.data_structure import Structure
from Modules.Tasks.BaseClases.date_label import DateLabel
from Modules.Tasks.global_task.model import ModelGlob
from Modules.Tasks.departments.model import ModelDep

# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QDateEdit
from Widgets.ComboBox import MYComboBox
from Widgets.DateEdit import MYDateEdit
from Widgets.Label import MYLabel
from Widgets.Widget import MYWidget







class BaseUIAttribsDep(MYWidget):

    # роль
    Editable = 0
    NotEditable = 1

    def __init__(self, DB, role=Editable, parent=None):
        super(BaseUIAttribsDep, self).__init__(
            parent=parent,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=10
        )

        self.__init_Attributes(role, DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()



    # inits
    def __init_Attributes(self, role, DB):
        self.__structure = Structure()
        self.__model_dep = ModelDep(data_base=DB)
        self.__model_task = ModelGlob(data_base=DB)
        self.__uitype = role

        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_name = MYLabel(parent=self, bold=True, text='Отдел:')
        self.__lbl_task = MYLabel(parent=self, bold=True, text='Поручение:')
        self.__lbl_date_start = MYLabel(parent=self, bold=True, text='Дата начала:')
        self.__lbl_date_finish = MYLabel(parent=self, bold=True, text='Дата отчёта:')
        self.__lbl_state = MYLabel(parent=self, bold=True, text='Состояние:')
        self.__descript = QTextBrowser(self)

        if self.__uitype == self.Editable:
            self.__name = MYComboBox(parent=self)
            self.__task = MYComboBox(parent=self)
            self.__date_start = MYDateEdit(self)
            self.__date_finish = MYDateEdit(self)
            self.__state = QCheckBox(self)
        else:
            self.__name = MYLabel(parent=self)
            self.__task = MYLabel(parent=self)
            self.__date_start = DateLabel(parent=self)
            self.__date_finish = DateLabel(parent=self)
            self.__state = MYLabel(parent=self, bold=False, italic=True)

    def __init_Parameters(self):
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

        if self.__uitype == self.Editable:
            self.__date_start.setCalendarPopup(True)
            self.__date_finish.setCalendarPopup(True)
            self.__name.setModel(self.__model_dep)
            self.__task.setModel(self.__model_task)
        self.__load_Descrition()

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole


        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_name)
        self.__form_layout.setWidget(1, AS_LABEL, self.__lbl_date_start)
        self.__form_layout.setWidget(2, AS_LABEL, self.__lbl_date_finish)
        self.__form_layout.setWidget(3, AS_LABEL, self.__lbl_task)
        self.__form_layout.setWidget(4, AS_LABEL, self.__lbl_state)

        self.__form_layout.setWidget(0, AS_FIELD, self.__name)
        self.__form_layout.setWidget(1, AS_FIELD, self.__date_start)
        self.__form_layout.setWidget(2, AS_FIELD, self.__date_finish)
        self.__form_layout.setWidget(3, AS_FIELD, self.__task)
        self.__form_layout.setWidget(4, AS_FIELD, self.__state)

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addWidget(self.__descript)
        self.main_layout.addLayout(self.btns_layout)

    def __init_Connects(self):
        if self.__uitype == self.Editable:
            self.__task.currentIndexChanged.connect(self.__load_Descrition)



    # class tools
    def __tool_SetState(self, state=0):
        if state == 0 or state == False or state == 'Невыполнено':
            if self.__uitype == self.Editable:
                self.__state.setCheckState(Qt.Unchecked)
            else:
                self.__state.setText('Невыполнено')
        else:
            if self.__uitype == self.Editable:
                self.__state.setCheckState(Qt.Checked)
            else:
                self.__state.setText('Выполнено')



    def __load_Descrition(self):
        if self.__uitype == self.Editable:
            task_name = self.__task.currentText()
        else:
            task_name = self.__task.text()

        for row in range(self.__model_task.rowCount()):
            data = self.__model_task.getStructure(row)
            name = data.name
            if task_name == name:
                descript = data.task
                self.__descript.setText(descript)
                break

    def __tool_SetName(self, name):
        name = str(name)
        self.__structure.setName(name)
        if self.__uitype == self.Editable:
            self.__name.setCurrentText(name)
        else:
            self.__name.setText(name)

    def __tool_SetTask(self, task):
        task = str(task)
        self.__structure.setTask(task)
        if self.__uitype == self.Editable:
            self.__task.setCurrentText(task)
        else:
            self.__task.setText(task)

    def __tool_SetDateStart(self,  qdatetime):
        self.__structure.setQDateTimeStart(qdatetime)
        self.__date_start.setDate(qdatetime.date())

    def __tool_SetDateFinish(self, qdatetime):
        self.__structure.setQDateTimeFinish(qdatetime)
        self.__date_finish.setDate(qdatetime.date())




    @property
    def dataStructure(self):
        if self.__uitype == self.Editable:
            name = self.__name.currentText()
            task = self.__task.currentText()
            dstart = self.__date_start.date()
            dfinish = self.__date_finish.date()
            if self.__state.isChecked():
                state = 1
            else:
                state = 0
        else:
            name = self.__name.text()
            task = self.__task.text()
            dstart = self.__date_start.date
            dfinish = self.__date_finish.date
            if self.__state.text() == 'Невыполнено':
                state = 0
            else:
                state = 1

        time = QTime().currentTime()
        sdatetime = QDateTime()
        sdatetime.setDate(dstart)
        sdatetime.setTime(time)

        fdatetime = QDateTime()
        fdatetime.setDate(dfinish)
        fdatetime.setTime(time)

        # print('name = ', name)
        # print('task = ', task)
        # print('dstart = ', dstart)
        # print('dfinish = ', dfinish)
        self.__structure.setName(name)
        self.__structure.setTask(task)
        self.__structure.setQDateTimeStart(sdatetime)
        self.__structure.setQDateTimeFinish(fdatetime)
        self.__structure.setState(state)
        return self.__structure


    # METHODS
    def setDataStructure(self, struct):
        self.__tool_SetName(struct.name)
        self.__tool_SetTask(struct.task)
        self.__tool_SetDateStart(struct.qDateTimeStart)
        self.__tool_SetDateFinish(struct.qDateTimeFinish)
        self.__tool_SetState(struct.state)
        self.__load_Descrition()


    def updateModel(self):
        self.__model_dep.select()
        self.__model_task.select()




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtSql import QSqlDatabase
    from paths import DB_FILE_PATH

    app = QApplication([])
    DATABASE = QSqlDatabase('QSQLITE')
    DATABASE.setDatabaseName(DB_FILE_PATH)
    DATABASE.open()
    win = BaseUIAttribsDep(DB=DATABASE, role=BaseUIAttribsDep.Editable)
    win.show()
    sys.exit(app.exec_())