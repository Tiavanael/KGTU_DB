
from Modules.Emloyees.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog




class FormEdit(MYDialog):

    def __init__(self, DB, parent=None):
        super(FormEdit, self).__init__(
            parent=parent,
            title='Редактирование сотрудника'
        )
        self.attribs = BaseUIAttribs(DB=DB, role=BaseUIAttribs.Editable, parent=self)
        self.main_layout.addWidget(self.attribs)
        self.resize(470, 190)







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormEdit()
    win.show()
    app.exec_()

