# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:

from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

from parameters      import ENABLE_STYLES
from style import STYLE


class MYFrame(QFrame):
    def __init__(self,
                 parent=None,
                 layout='V',
                 layout_margins=[0, 0, 0, 0],
                 layout_spacing=5,
                 spliter=None,
                 spliter_margins=[0, 0, 0, 0],
                 line_width=0
                 ):
        super(MYFrame, self).__init__()
        if parent: self.setParent(parent)

        if layout == 'V':
            self.main_layout = QVBoxLayout(self)
            self.main_spacer = QSpacerItem(20, 40,
                                           QSizePolicy.Minimum,
                                           QSizePolicy.Expanding)
        elif layout == 'H':
            self.main_layout = QHBoxLayout(self)
            self.main_spacer = QSpacerItem(20, 40,
                                           QSizePolicy.Expanding,
                                           QSizePolicy.Minimum)
        elif layout == 'G':
            self.main_layout = QGridLayout(self)
            self.main_spacer_vertical = QSpacerItem(20, 40,
                                                    QSizePolicy.Minimum,
                                                    QSizePolicy.Expanding)
            self.main_spacer_horizontal = QSpacerItem(20, 40,
                                                      QSizePolicy.Expanding,
                                                      QSizePolicy.Minimum)



        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Plain)
        self.setLineWidth(line_width)

        self.main_layout.setSpacing(layout_spacing)
        self.main_layout.setContentsMargins(layout_margins[0],
                                            layout_margins[1],
                                            layout_margins[2],
                                            layout_margins[3]
                                            )
        if layout == 'V' or layout == 'H':
            if spliter:
                if spliter == 'V': self.main_spliter = QSplitter(Qt.Vertical)
                elif spliter == 'H': self.main_spliter = QSplitter(Qt.Horizontal)
                self.main_spliter.setContentsMargins(spliter_margins[0],
                                                     spliter_margins[1],
                                                     spliter_margins[2],
                                                     spliter_margins[3]
                                                     )
                self.main_layout.addWidget(self.main_spliter)

        #self.setStyleSheet(STYLE.Frame)

        if ENABLE_STYLES: self.setStyleSheet(STYLE.Frame)