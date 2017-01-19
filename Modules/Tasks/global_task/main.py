from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QVBoxLayout

from DataBase.access_model import DBAccessModel
from Modules.Tasks.global_task.base_ui_attribs import BaseUIAttribs
from Modules.Tasks.global_task.form_add import FormAdd
from Modules.Tasks.global_task.form_edit import FormEdit
from Modules.Tasks.global_task.model import ModelGlob
from Widgets.PushButton import MYPushButton
from Widgets.TableView import MYTableView
from Widgets.Widget import MYWidget
from icons import ICON






class GlobalTasks(MYWidget):

    #inits
    def __init__(self, DB):
        super(GlobalTasks, self).__init__(
            layout='H',
            layout_margins=[10, 10, 10, 10]
        )

        self.__init_Layouts()
        self.__init_Widgets(DB)
        self.__init_Parameters()
        self.__init_Layouting()
        self.__init_Connects()


    def __init_Layouts(self):
        self.__btn_layout = QHBoxLayout()
        self.__list_layout = QVBoxLayout()

    def __init_Widgets(self, DB):
        self.__model = ModelGlob(data_base=DB)
        self.__form_add = FormAdd()
        self.__form_edit = FormEdit()
        self.__form_view = BaseUIAttribs(BaseUIAttribs.NotEditable)
        self.__list = MYTableView(parent=self)
        self.__btn_add = MYPushButton(parent=self)
        self.__btn_remove = MYPushButton(parent=self)

    def __init_Parameters(self):
        self.__list.setModel(self.__model)
        self.__list.hideColumn(1)
        self.__btn_add.setIcon(QIcon(ICON.DEFAULT.add()))
        self.__btn_remove.setIcon(QIcon(ICON.DEFAULT.remove()))

    def __init_Layouting(self):
        self.__list_layout.addLayout(self.__btn_layout)
        self.__list_layout.addWidget(self.__list)
        self.__btn_layout.addWidget(self.__btn_add)
        self.__btn_layout.addWidget(self.__btn_remove)
        self.main_layout.addLayout(self.__list_layout)
        self.main_layout.addWidget(self.__form_view)

    def __init_Connects(self):
        self.__list.clicked.connect(self.__load_FormView)
        self.__list.doubleClicked.connect(self.__open_EditForm)
        self.__btn_add.clicked.connect(self.__open_AddForm)
        self.__btn_remove.clicked.connect(self.__remove)
        self.__form_add.accepted.connect(self.__add)
        self.__form_edit.accepted.connect(self.__edit)



    def __load_FormView(self, index):
        row = index.row()
        data = self.__model.getStructure(row)
        self.__form_view.setDataStructure(data)

    def __open_AddForm(self):
        self.__form_add.show()

    def __open_EditForm(self, index):
        row = index.row()
        data = self.__model.getStructure(row)
        self.__form_edit.attribs.setDataStructure(data)
        self.__form_edit.show()

    def __add(self):
        data = self.__form_add.attribs.dataStructure
        self.__model.addRecord(data)

    def __edit(self):
        index = self.__list.selectedIndexes()[0]
        row = index.row()
        data = self.__form_edit.attribs.dataStructure

        self.__model.editRecord(data, row)
        self.__load_FormView(index)

    def __remove(self):
        selected = self.__list.selectedIndexes()
        if selected:
            index = selected[0]
            row = index.row()
            self.__model.removeRecord(row)

