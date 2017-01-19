

from PyQt5.QtGui import QIcon
from Widgets.PushButton import MYPushButton
from icons import ICON
from Modules.Events.BaseClases.base_ui_attribs import BaseUIAttribs





class FormView(BaseUIAttribs):

    def __init__(self, DB, parent=None):
        super(FormView, self).__init__(
            parent=parent,
            role=self.NotEditable,
            DB=DB
        )
        self.btn_add = MYPushButton(parent=self)
        self.btn_remove = MYPushButton(parent=self)

        self.btn_add.setIcon(QIcon(ICON.DEFAULT.add()))
        self.btn_remove.setIcon(QIcon(ICON.DEFAULT.remove()))

        self.btns_layout.addWidget(self.btn_add)
        self.btns_layout.addWidget(self.btn_remove)
        self.setFixedWidth(300)



if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormView()
    win.show()
    app.exec_()

