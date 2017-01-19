# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:



from PyQt5.QtWidgets import QCheckBox

from parameters import ENABLE_STYLES
from style import STYLE


class MYChekBox(QCheckBox):
    def __init__(self, parent=None, text=''):
        super(MYChekBox, self).__init__()
        if parent: self.setParent(parent)
        if text != '': self.setText(text)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.CheckBox)