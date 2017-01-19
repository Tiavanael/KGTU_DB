# Qt Types
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QTextBrowser

from Modules.Tasks.global_task.data_structure import GlobalTaskStructure as Structure


# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from Widgets.Label import MYLabel
from Widgets.LineEdit import MYLineEdit
from Widgets.TextEdit import MYTextEdit
from Widgets.Widget import MYWidget







class BaseUIAttribs(MYWidget):

    # роль
    Editable = 0
    NotEditable = 1

    def __init__(self, role=Editable, parent=None):
        super(BaseUIAttribs, self).__init__(
            parent=parent,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=10
        )

        self.__init_Attributes(role)
        self.__init_Parameters()
        self.__init_Layouting()


    def __init_Attributes(self, role):
        self.__structure = Structure()
        self.__uitype = role

        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_name = MYLabel(parent=self, bold=True, text='Название:')

        if self.__uitype == self.Editable:
            self.__name = MYLineEdit(parent=self)
            self.__task = MYTextEdit(parent=self)
        else:
            self.__name = MYLabel(parent=self)
            self.__task = QTextBrowser(self)

    def __init_Parameters(self):
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole


        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_name)

        self.__form_layout.setWidget(0, AS_FIELD, self.__name)

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addWidget(self.__task)
        self.main_layout.addLayout(self.btns_layout)
        # self.main_layout.addItem(self.main_spacer)



    def __tool_SetName(self, name):
        name = str(name)
        self.__structure.setName(name)
        self.__name.setText(name)

    def __tool_SetTask(self, task):
        task = str(task)
        self.__structure.setTask(task)
        self.__task.setText(task)




    @property
    def dataStructure(self):
        if self.__uitype == self.Editable:
            name = self.__name.text()
            task = self.__task.toPlainText()
        else:
            name = self.__name.text()
            task = self.__task.toPlainText()

        self.__structure.setName(name)
        self.__structure.setTask(task)

        return self.__structure


    def setDataStructure(self, struct):
        self.__tool_SetName(struct.name)
        self.__tool_SetTask(struct.task)







if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtSql import QSqlDatabase
    from paths import DB_FILE_PATH

    app = QApplication([])
    DATABASE = QSqlDatabase('QSQLITE')
    DATABASE.setDatabaseName(DB_FILE_PATH)
    DATABASE.open()
    win = BaseUIAttribs(role=BaseUIAttribs.Editable)
    win.show()
    sys.exit(app.exec_())