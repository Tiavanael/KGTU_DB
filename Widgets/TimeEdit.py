from PyQt5.QtWidgets import QTimeEdit


class MYTimeEdit(QTimeEdit):
    def __init__(self, parent=None):
        super(MYTimeEdit, self).__init__()
        if parent: self.setParent(parent)
        self.setTime(self.time().currentTime())


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    win = MYTimeEdit()
    win.show()
    sys.exit(app.exec_())