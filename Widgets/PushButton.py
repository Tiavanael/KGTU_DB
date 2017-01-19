from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton

from parameters      import ENABLE_STYLES
from style import STYLE


class MYPushButton(QPushButton):
    def __init__(self,
                 parent=None,
                 text=''):
        super(MYPushButton, self).__init__()
        if parent: self.setParent(parent)
        if text: self.setText(text)
        self.setFixedHeight(30)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.PushButton)
        self.setIconSize(QSize(25, 25))