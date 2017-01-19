


from Modules.Events.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog





class FormEdit(MYDialog):

    def __init__(self, DB, parent=None):
        super(FormEdit, self).__init__(
            parent=parent,
            title='Редактирование дела',
        )
        self.attribs = BaseUIAttribs(DB, BaseUIAttribs.Editable, self)
        self.main_layout.addWidget(self.attribs)






if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormEdit()
    win.show()
    app.exec_()

