

from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QLineEdit

from parameters      import ENABLE_STYLES
from style import STYLE


class MYLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MYLineEdit, self).__init__()
        if parent: self.setParent(parent)
        # self.setFixedHeight(30)
        self.setAlignment(Qt.AlignVCenter)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.LineEdit)
