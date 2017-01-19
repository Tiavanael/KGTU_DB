

from Modules.Tasks.employees.attrib_ui import BaseUIAttribsEmp
from Widgets.Dialog import MYDialog








class FormAdd(MYDialog):

    def __init__(self, DB, parent=None):
        super(FormAdd, self).__init__(
            parent=parent,
            title='Добавление дела',
        )
        self.attribs = BaseUIAttribsEmp(
            DB=DB,
            role=BaseUIAttribsEmp.Editable,
            parent=self
        )
        self.main_layout.addWidget(self.attribs)


    def setFIO(self, name):
        self.attribs.setFIO(name)







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormAdd()
    win.show()
    app.exec_()

