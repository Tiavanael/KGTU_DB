from PyQt5.QtWidgets import QTextEdit

from Modules.Tasks.global_task.base_ui_attribs import BaseUIAttribs
from Widgets.Dialog import MYDialog
from Widgets.LineEdit import MYLineEdit


class FormAdd(MYDialog):

    #inits
    def __init__(self):
        super(FormAdd, self).__init__(
            title='Новое поручение'
        )
        self.attribs = BaseUIAttribs(role=BaseUIAttribs.Editable)
        self.main_layout.addWidget(self.attribs)
    
    
    
    
    
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = FormAdd()
    win.show()
    sys.exit(app.exec_())