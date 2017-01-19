



from Modules.Contacts.BaseClases.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog




class FormEdit(MYDialog):

    def __init__(self, parent=None):
        super(FormEdit, self).__init__(
            parent=parent,
            title='Редактирование контакта'
        )
        self.attribs = BaseUIAttribs(BaseUIAttribs.Editable)
        self.main_layout.addWidget(self.attribs)
        self.resize(440, 190)







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormEdit()
    win.show()
    app.exec_()

