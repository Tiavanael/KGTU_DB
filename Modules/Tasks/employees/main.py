from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from Modules.Tasks.employees.form_add import FormAdd
from Modules.Tasks.employees.form_edit import FormEdit
from Modules.Tasks.employees.model import ModelEmpTask
from Utility.ReportClass import Report
from Widgets.ComboBox import MYComboBox
from Widgets.DateEdit import MYDateEdit
from Widgets.PushButton import MYPushButton
from Widgets.TableView import MYTableView
from Widgets.Widget import MYWidget
from Modules.Tasks.employees.form_view import FormView


class EmployeeTask(MYWidget):

    #inits
    def __init__(self, DB):
        super(EmployeeTask, self).__init__(
            layout='H',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()

    def __init_Attributes(self, DB):


        self.__report_filter = 0
        self.__Report = Report(name="Отчет по поручениям сотрудникам")
        self.__layout_filters = QHBoxLayout()
        self.__layout_list = QVBoxLayout()
        self.__report_layout = QHBoxLayout()
        self.__btn_report_add = MYPushButton(parent=self, text='Добавить в отчёт')
        self.__btn_report = MYPushButton(parent=self, text='Отчёт')
        self.__btn_filter_all = MYPushButton(parent=self, text='Все')
        self.__btn_filter_today = MYPushButton(parent=self, text='На сегодня')
        self.__btn_filter_nevipoln = MYPushButton(parent=self, text='Невыполненые')
        self.__btn_filter_proval = MYPushButton(parent=self, text='Провальные')
        self.__btn_filter_vipoln = MYPushButton(parent=self, text='Выполненные')
        self.__btn_filter_day = MYDateEdit(parent=self)

        self.__form_view = FormView(DB, self)
        self.__form_add = FormAdd(DB, self)
        self.__form_edit = FormEdit(DB, self)

        self.__model = ModelEmpTask(data_base=DB)
        self.__list = MYTableView()

    def __init_Parameters(self):
        self.__list.setModel(self.__model)
        # self.__list.hideColumn(1)
        self.__list.hideColumn(2)
        self.__list.hideColumn(3)
        self.__list.hideColumn(4)
        self.__list.hideColumn(5)
        self.__list.setColumnWidth(0, 250)

    def __init_Layouting(self):
        self.__layout_filters.addWidget(self.__btn_filter_all)
        self.__layout_filters.addWidget(self.__btn_filter_today)
        self.__layout_filters.addWidget(self.__btn_filter_nevipoln)
        self.__layout_filters.addWidget(self.__btn_filter_proval)
        self.__layout_filters.addWidget(self.__btn_filter_vipoln)
        self.__layout_filters.addWidget(self.__btn_filter_day)
        self.__layout_list.addLayout(self.__layout_filters)
        self.__layout_list.addWidget(self.__list)
        self.__report_layout.addWidget(self.__btn_report_add)
        self.__report_layout.addWidget(self.__btn_report)
        self.__layout_list.addLayout(self.__report_layout)
        self.main_layout.addLayout(self.__layout_list)
        self.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__list.clicked.connect(self.__load_attribs)
        self.__list.doubleClicked.connect(self.__open_FormEdit)
        self.__form_view.btn_add.clicked.connect(self.__open_FormAdd)
        self.__form_view.btn_remove.clicked.connect(self.__remove)
        self.__form_edit.accepted.connect(self.__edit)
        self.__form_add.accepted.connect(self.__add)
        self.__btn_filter_all.clicked.connect(self.__filter_All)
        self.__btn_filter_today.clicked.connect(self.__filter_ToDay)
        self.__btn_filter_day.dateChanged.connect(self.__filter_SpecDate)
        self.__btn_filter_vipoln.clicked.connect(self.__filter_Vipoln)
        self.__btn_filter_nevipoln.clicked.connect(self.__filter_Nevipoln)
        self.__btn_filter_proval.clicked.connect(self.__filter_Proval)

        self.__btn_report.clicked.connect(self.__report_Print)
        self.__btn_report_add.clicked.connect(self.__report_Add)



    def __load_attribs(self, index):
        row = index.row()
        data = self.__model.getStructure(row)
        self.__form_view.setDataStructure(data)


    def __report_Add(self):

        indexes = [5]
        if self.__report_filter == 0:
            self.__Report.addString("Все поручения")
        elif self.__report_filter == 1:
            self.__Report.addString("Поручения на сегодня")
            indexes += [2, 3]
        elif self.__report_filter == 2:
            self.__Report.addString("Поручения на " + str(self.__btn_filter_day.dateTime().date().toPyDate()))
            indexes += [2, 3]
        elif self.__report_filter == 3:
            self.__Report.addString("Выполненые поручения")
            indexes += [4]
        elif self.__report_filter == 4:
            self.__Report.addString("Не выполненые поручения")
            indexes += [4]
        elif self.__report_filter == 5:
            self.__Report.addString("Просроченные поручения")
            indexes += [4]

        def getState(nnn):
            if nnn == 0:
                return "Не выполнен"
            elif nnn == 1:
                return "Выполнено"

        self.__Report.addTableFromModel(
            model=self.__model,
            fieldsNames=["ФИО","Задание","Начало","Окончание","Выполнение"],
            fieldsIndexes=indexes,
            delegates={4:getState}
        )

    def __report_Print(self):
        self.__Report.showPreview()

    def __open_FormEdit(self, index):
        self.__form_edit.attribs.updateModel()
        row = index.row()
        data = self.__model.getStructure(row)
        self.__form_edit.attribs.setDataStructure(data)
        self.__form_edit.exec_()

    def __open_FormAdd(self):
        self.__form_add.updatesEnabled()
        self.__form_add.attribs.updateModel()
        self.__form_add.exec_()

    def __filter_All(self):
        self.__model.setFilter('')
        self.__model.select()
        self.__report_filter = 0

    def __filter_ToDay(self):
        d = self.__btn_filter_day.date().currentDate()
        self.__btn_filter_day.setDate(d)
        self.__model.setDateTimeFilter('==')
        self.__model.select()
        self.__report_filter = 1

    def __filter_SpecDate(self):
        dt = self.__btn_filter_day.dateTime()
        self.__model.setDateTimeFilter(
            compare_sign='==',
            field='datetime_start',
            type='d',
            date=dt
        )
        self.__model.select()
        self.__report_filter = 2

    def __filter_Vipoln(self):
        self.__model.setFilter('state == 1')
        self.__model.select()
        self.__report_filter = 3

    def __filter_Nevipoln(self):
        self.__model.setFilter('state == 0')
        self.__model.select()
        self.__report_filter = 4

    def __filter_Proval(self):
        self.__model.setDateTimeFilter(
            compare_sign="<=",
            field='datetime_finish',
            type='d',
        )
        self.__model.setFilter(self.__model.filter() + ' and state == 0')
        self.__report_filter = 5
        self.__report_filter = 5

    def __edit(self):
        selected = self.__list.selectedIndexes()
        if selected:
            index = selected[0]
            data = self.__form_edit.attribs.dataStructure
            row = index.row()
            self.__model.editRecord(data, row)
            self.__load_attribs(index)

    def __add(self):
        data = self.__form_add.attribs.dataStructure
        self.__model.addRecord(data)
        self.__model.select()

    def __remove(self):
        selected = self.__list.selectedIndexes()
        if selected:
            index = selected[0]
            self.__model.removeRecord(index.row())

    #SLOT
    def createEmployeeTask(self, name):
        self.__form_add.setFIO(name)
        self.__form_add.attribs.updateModel()
        self.__form_add.show()


















if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtSql import QSqlDatabase
    from paths import DB_FILE_PATH

    app = QApplication([])
    DATABASE = QSqlDatabase('QSQLITE')
    DATABASE.setDatabaseName(DB_FILE_PATH)
    DATABASE.open()
    win = EmployeeTask(DATABASE)
    win.show()
    sys.exit(app.exec_())