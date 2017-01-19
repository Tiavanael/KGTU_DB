

from Modules.Tasks.departments.attrib_ui import BaseUIAttribsDep
from Widgets.Dialog import MYDialog








class FormEdit(MYDialog):

    def __init__(self, DB, parent=None):
        super(FormEdit, self).__init__(
            parent=parent,
            title='Добавление дела',
        )
        self.attribs = BaseUIAttribsDep(
            DB=DB,
            role=BaseUIAttribsDep.Editable,
            parent=self
        )
        self.main_layout.addWidget(self.attribs)



if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormAdd()
    win.show()
    app.exec_()

