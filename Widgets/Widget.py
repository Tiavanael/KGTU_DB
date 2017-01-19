# -*- coding: utf-8 -*-


#Qt namespace
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QSplitter
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

from Widgets.Spacer  import MYSpacer
from parameters      import ENABLE_STYLES
from style import STYLE








class MYWidget(QWidget):
    def __init__(
            self,
            parent=None,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=5,
            spliter=None,
            spliter_margins=[0, 0, 0, 0]
    ):

        super(MYWidget, self).__init__()

        if parent: self.setParent(parent)

        if layout == 'V':
            self.main_layout = QVBoxLayout(self)
            self.main_spacer = MYSpacer('V')

        elif layout == 'H':
            self.main_layout = QHBoxLayout(self)
            self.main_spacer = MYSpacer('H')

        elif layout == 'G':
            self.main_layout            = QGridLayout(self)
            self.main_spacer_vertical   = MYSpacer('V')
            self.main_spacer_horizontal = MYSpacer('H')

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

        if ENABLE_STYLES: self.setStyleSheet(STYLE.Widget)

