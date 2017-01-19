from PyQt5.QtWidgets import QDateEdit


class MYDateEdit(QDateEdit):
    def __init__(self, parent=None):
        super(MYDateEdit, self).__init__()
        if parent: self.setParent(parent)
        self.setCalendarPopup(True)
        self.setDate(self.date().currentDate())
        
        
        
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    win = MYDateEdit()
    win.show()
    sys.exit(app.exec_())