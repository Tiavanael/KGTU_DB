from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from Widgets.DateEdit import MYDateEdit
from Widgets.Label import MYLabel
from Widgets.LineEdit import MYLineEdit
from Widgets.PushButton import MYPushButton
from Widgets.Widget import MYWidget

from Modules.Notes.form_add import FormAdd
from Modules.Notes.form_edit import FormEdit
from Modules.Notes.form_view import FormView
from Modules.Notes.BaseClases.model import Model
from Modules.Notes.BaseClases.base_ui_list import BaseUIList
from PyQt5.QtGui import QIcon
from icons import ICON







class Notes(MYWidget):


    def __init__(self, DB):
        super(Notes, self).__init__(
            layout='H',
            layout_margins=[10, 10, 10, 10],
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()
        # self.fill()


    #inits
    def __init_Attributes(self, DB):
        self.__poisk_layout = QHBoxLayout()
        self.__poisk_lbl = MYLabel(parent=self, bold=True, text='Поиск')
        self.__poisk_line = MYLineEdit(parent=self)
        self.__btn_all = MYPushButton(parent=self, text='Все')
        self.__btn_today = MYPushButton(parent=self, text='На сегодня')
        self.__date_filter = MYDateEdit(parent=self)
        self.__layout_list = QVBoxLayout()
        self.__layout_filters = QHBoxLayout()
        self.__model = Model(DB)
        self.__list = BaseUIList(parent=self, model=self.__model)
        self.__form_view = FormView(self)
        self.__form_add  = FormAdd(self)
        self.__form_edit = FormEdit(self)

    def __init_Parameters(self):
        self.resize(500, 620)
        self.__list.setModel(self.__model)

    def __init_Layouting(self):
        self.__poisk_layout.addWidget(self.__poisk_lbl)
        self.__poisk_layout.addWidget(self.__poisk_line)
        self.__layout_filters.addWidget(self.__btn_all)
        self.__layout_filters.addWidget(self.__btn_today)
        self.__layout_filters.addWidget(self.__date_filter)
        self.__layout_list.addLayout(self.__poisk_layout)
        self.__layout_list.addLayout(self.__layout_filters)
        self.__layout_list.addWidget(self.__list)
        self.main_layout.addLayout(self.__layout_list)
        self.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__list.doubleClicked.connect(self.__tool_OpenEditForm)
        self.__form_edit.accepted.connect(self.__tool_EditContact)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentContact)
        self.__form_add.accepted.connect(self.__tool_AddNewContact)
        self.__list.clicked.connect(self.__tool_LoadAttribsToViewForm)
        self.__form_view.btn_add.clicked.connect(self.__tool_OpenAddForm)
        self.__btn_all.clicked.connect(self.__filter_All)
        self.__btn_today.clicked.connect(self.__filter_Today)
        self.__date_filter.dateChanged.connect(self.__filter_SpecificDate)
        self.__poisk_line.textChanged.connect(self.__poisk_Specific)



    def __poisk_Specific(self):
        field = 'theme'
        text = self.__poisk_line.text()
        self.__model.setPoisk(field, text)

    def __filter_All(self):
        self.__model.setFilter('')
        self.__model.select()

    def __filter_SpecificDate(self):
        d = self.__date_filter.date()
        t = QTime(0, 0)
        dt = QDateTime()
        dt.setDate(d)
        dt.setTime(t)
        self.__model.setDateTimeFilter(type='d', compare_sign='==', date=dt)
        self.__model.select()

    def __filter_Today(self):
        self.__model.setDateTimeFilter('==')
        self.__model.select()



    # class tool
    def __tool_LoadAttribsToViewForm(self, index):
        row = index.row()
        structure = self.__model.getStructure(row)
        # print(structure.asFieldsForRecord)
        self.__form_view.setDataStructure(structure)

    def __tool_EditContact(self):
        index = self.__list.selectedIndexes()
        if index:
            index = index[0]
            row = index.row()
        new_structure = self.__form_edit.attribs.dataStructure
        self.__model.editRecord(data_structure=new_structure, row=row)
        self.__tool_LoadAttribsToViewForm(index)

    def __tool_AddNewContact(self):
        structure = self.__form_add.attribs.dataStructure
        self.__model.addRecord(data_structure=structure)

    def __tool_OpenEditForm(self):
        data_structure = self.__form_view.dataStructure
        self.__form_edit.attribs.setDataStructure(data_structure)
        self.__form_edit.exec_()
    
    def __tool_OpenAddForm(self):
        self.__form_add.exec_()

    def __tool_RemoveCurrentContact(self):
        index = self.__list.selectedIndexes()
        if index:
            index = index[0]
            row = index.row()
            self.__model.removeRecord(row)

