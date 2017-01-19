# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:



from PyQt5.QtCore    import Qt, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListView

from parameters import ENABLE_STYLES
from parameters import FONT_SIZE
from style import STYLE


class MYListView(QListView):

    #SIGNALS
    itemClicked = pyqtSignal(str)

    #INIT
    def __init__(self, parent=None):
        super(MYListView, self).__init__()
        self.clicked.connect(self.__EMITT_itemClicked)

        #PARMS
        if parent: self.setParent(parent)

        font = QFont()
        font.setPointSize(FONT_SIZE)

        self.setFont(font)

        if ENABLE_STYLES: self.setStyleSheet(STYLE.ListWidget)

    def __EMITT_itemClicked(self, index):
        self.itemClicked.emit(index.data(Qt.DisplayRole))