# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:



from PyQt5.QtWidgets import QListWidget

from parameters      import ENABLE_STYLES
from style import STYLE


class MYListWidget(QListWidget):
    def __init__(self, parent=None):
        super(MYListWidget, self).__init__()
        if parent: self.setParent(parent)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.ListWidget)