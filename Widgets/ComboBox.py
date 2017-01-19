# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:

from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt

from parameters import ENABLE_STYLES
from style import STYLE


class MYComboBox(QComboBox):
    def __init__(self, parent):
        super(MYComboBox, self).__init__()
        if parent:
            self.setParent(parent)
        # self.setFixedHeight(30)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.ComboBox)

    def updateList(self, new_list):
        current = self.currentText()
        self.clear()
        self.addItems(new_list)
        if current in new_list:
            index = new_list.index(current)
            self.setCurrentIndex(index)

    def renameCurrentItem(self, new_name):
        lst = []
        current_text = self.currentText()
        for index in range(self.count()):
            lst.append(self.itemText(index))

        lst.remove(current_text)
        lst.append(new_name)
        self.clear()
        self.addItems(lst)
        self.setCurrentIndex(len(lst) - 1)

    def setCurrentText(self, text):
        for index in range(self.count()):
            item_text = self.itemText(index)
            if item_text == text:
                self.setCurrentIndex(index)
                break