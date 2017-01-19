# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:




from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from parameters import ENABLE_STYLES
from parameters import FONT_SIZE
from style import STYLE


class MYLabel(QLabel):
    def __init__(
            self,
            parent=None,
            text='',
            bold=False,
            italic=False
    ):
        super(MYLabel, self).__init__()
        if parent: self.setParent(parent)
        if text: self.setText(text)

        font = QFont()
        # font.setPointSize(FONT_SIZE)
        font.setBold(bold)
        font.setItalic(italic)
        self.setFont(font)

        if ENABLE_STYLES: self.setStyleSheet(STYLE.Label)