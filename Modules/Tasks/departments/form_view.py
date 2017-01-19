

from PyQt5.QtGui import QIcon
from Widgets.PushButton import MYPushButton
from icons import ICON
from Modules.Tasks.departments.attrib_ui import BaseUIAttribsDep





class FormView(BaseUIAttribsDep):

    def __init__(self, DB, parent=None):
        super(FormView, self).__init__(
            parent=parent,
            role=self.NotEditable,
            DB=DB
        )
        self.setFixedWidth(350)
        self.btn_add = MYPushButton(parent=self)
        self.btn_remove = MYPushButton(parent=self)

        self.btn_add.setIcon(QIcon(ICON.DEFAULT.add()))
        self.btn_remove.setIcon(QIcon(ICON.DEFAULT.remove()))

        self.btns_layout.addWidget(self.btn_add)
        self.btns_layout.addWidget(self.btn_remove)







if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtSql import QSqlDatabase
    from paths import DB_FILE_PATH

    app = QApplication([])
    DATABASE = QSqlDatabase('QSQLITE')
    DATABASE.setDatabaseName(DB_FILE_PATH)
    DATABASE.open()
    win = FormView(DB=DATABASE)
    win.show()
    sys.exit(app.exec_())

