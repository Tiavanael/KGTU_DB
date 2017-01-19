


from PyQt5.QtGui import QIcon
from Widgets.PushButton import MYPushButton
from icons import ICON
from Modules.Contacts.BaseClases.base_ui_attribs import BaseUIAttribs

from Widgets.Dialog import MYDialog






class FormAdd(MYDialog):

    def __init__(self, parent=None):
        super(FormAdd, self).__init__(
            title='Добавление контакта',
            parent=parent
        )
        self.attribs = BaseUIAttribs(BaseUIAttribs.Editable)
        self.main_layout.addWidget(self.attribs)
        self.resize(440, 190)








if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormAdd()
    win.show()
    app.exec_()

