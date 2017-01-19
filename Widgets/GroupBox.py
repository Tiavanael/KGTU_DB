# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:


#Qt namespace
from PyQt5.QtCore    import Qt


#Qt types
from PyQt5.QtGui     import QFont


#WIDGETS
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QSplitter
from Widgets.Spacer  import MYSpacer


#PARAMETERS
from parameters import ENABLE_STYLES
from parameters import FONT_SIZE


#STYLE
from style import STYLE






class MYGroupBox(QGroupBox):
    def __init__(
            self,
            parent=None,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=5,
            spliter=None,
            spliter_margins=[0, 0, 0, 0],
            title = ''
    ):

        super(MYGroupBox, self).__init__()

        if parent: self.setParent(parent)

        if layout == 'V':
            self.main_layout = QVBoxLayout(self)
            self.main_spacer = MYSpacer('V')

        elif layout == 'H':
            self.main_layout = QHBoxLayout(self)
            self.main_spacer = MYSpacer('H')

        elif layout == 'G':
            self.main_layout = QGridLayout(self)
            self.main_spacer_vertical = MYSpacer('V')
            self.main_spacer_horizontal = MYSpacer('H')



        self.main_layout.setSpacing(layout_spacing)
        self.main_layout.setContentsMargins(
            layout_margins[0],
            layout_margins[1],
            layout_margins[2],
            layout_margins[3]
        )

        self.main_layout.setSpacing(layout_spacing)
        self.main_layout.setContentsMargins(
            layout_margins[0],
            layout_margins[1],
            layout_margins[2],
            layout_margins[3]
        )

        if layout == 'V' or layout == 'H':
            if spliter:
                if   spliter == 'V': self.main_spliter = QSplitter(Qt.Vertical)
                elif spliter == 'H': self.main_spliter = QSplitter(Qt.Horizontal)

                self.main_spliter.setContentsMargins(
                    spliter_margins[0],
                    spliter_margins[1],
                    spliter_margins[2],
                    spliter_margins[3]
                )

                self.main_layout.addWidget(self.main_spliter)

        self.setTitle(title)


        font = QFont()
        font.setPointSize(FONT_SIZE)
        
        self.setFont(font)

        self.setStyleSheet(
            """
            QGroupBox
            {
                font: bold;
            }
            """
        )
        if ENABLE_STYLES: self.setStyleSheet(STYLE.GroupBox)