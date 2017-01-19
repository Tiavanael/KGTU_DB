
from PyQt5.QtWidgets import QHBoxLayout

from Widgets.ComboBox import MYComboBox
from Widgets.Label import MYLabel
from Widgets.LineEdit import MYLineEdit
from Widgets.Widget import MYWidget

from Modules.Contacts.form_add import FormAdd
from Modules.Contacts.form_edit import FormEdit
from Modules.Contacts.form_view import FormView
from Modules.Contacts.BaseClases.model import Model
from Modules.Contacts.BaseClases.base_ui_list import BaseUIList







class Contacts(MYWidget):
    def __init__(self, DB):
        super(Contacts, self).__init__(
            layout='V',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Attributes(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()


    #inits
    def __init_Attributes(self, DB):
        self.__filters_layout = QHBoxLayout()
        self.__poisk_layout = QHBoxLayout()
        self.__poisk_lbl = MYLabel(parent=self, bold=True, text='Поиск')
        self.__poisk_line = MYLineEdit(parent=self)
        self.__poisk_field = MYComboBox(parent=self)
        self.__model = Model(DB)
        self.__list = BaseUIList(parent=self, model=self.__model)
        self.__form_view = FormView(self)
        self.__form_add  = FormAdd(self)
        self.__form_edit = FormEdit(self)

    def __init_Parameters(self):
        self.__poisk_field.addItems(['Компания', 'ФИО'])
        self.resize(300, 620)
        self.__list.setModel(self.__model)

    def __init_Layouting(self):
        self.__poisk_layout.addWidget(self.__poisk_lbl)
        self.__poisk_layout.addWidget(self.__poisk_line)
        self.__poisk_layout.addWidget(self.__poisk_field)
        self.main_layout.addWidget(self.__form_view)
        self.main_layout.addLayout(self.__poisk_layout)
        self.main_layout.addLayout(self.__filters_layout)
        self.main_layout.addWidget(self.__list)

    def __init_Connects(self):
        self.__list.doubleClicked.connect(self.__tool_OpenEditForm)
        self.__form_edit.accepted.connect(self.__tool_EditContact)
        self.__form_view.btn_remove.clicked.connect(self.__tool_RemoveCurrentContact)
        self.__form_add.accepted.connect(self.__tool_AddNewContact)
        self.__list.clicked.connect(self.__tool_LoadAttribsToViewForm)
        self.__form_view.btn_add.clicked.connect(self.__tool_OpenAddForm)
        self.__poisk_line.textChanged.connect(self.__poisk_Specific)



    def __poisk_Specific(self):

        if self.__poisk_field.currentText() == 'ФИО':
            field = 'name'
        elif self.__poisk_field.currentText() == 'Компания':
            field = 'company'

        text = self.__poisk_line.text()

        self.__model.setPoisk(field, text)



    # class tool
    def __tool_LoadAttribsToViewForm(self, index):
        row = index.row()
        structure = self.__model.getStructure(row)
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
        # print(data_structure.asFieldsForRecord)
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
