# -*- coding: utf-8 -*-



#Qt types
from PyQt5.QtGui import QFont


#WIDGETS
from PyQt5.QtWidgets import QTreeWidget


#PARAMETERS
from parameters import ENABLE_STYLES
from parameters import FONT_SIZE


#STYLE
from style import STYLE








class MYTreeWidget(QTreeWidget):
    def __init__(self, parent=None):
        super(MYTreeWidget, self).__init__()


        # ATTRIBUTES------------------------------------------

        self.font = QFont()

        # END ATTRIBUTES--------------------------------------




        # PARMS-----------------------------------------------

        self.font.setPointSize(FONT_SIZE)
        self.setFont(self.font)

        if parent: self.setParent(parent)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.TreeWidget)

        # END PARMS-------------------------------------------



