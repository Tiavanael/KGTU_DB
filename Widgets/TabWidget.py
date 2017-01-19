# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:




from PyQt5.QtWidgets import QTabWidget, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout


class MYTabWidget(QTabWidget):
    def __init__(self, parent):
        super(MYTabWidget, self).__init__()
        self.setParent(parent)
        self.tab_dict = {} #{'tab_name':['index', 'widget', 'widg_layout']}

    #METHODES
    def createContent(self, tab_text, tab_layout='V', content=None):
        not_exist = self.add_tab(tab_text, tab_layout)
        if not_exist:
            content.setParent(self.getWidgetTab(tab_text))
            self.getTabLayout(tab_text).addWidget(content)

    def add_tab(self, tab_text, tab_layout='V'):
        if tab_text not in self.tab_dict:
            index = len(self.tab_dict)
            widget = QWidget()
            if tab_layout == 'V':
                layout = QVBoxLayout(widget)
                layout.setContentsMargins(1, 1, 1, 1)
                self.tab_dict[tab_text] = [index, widget, layout]
            elif tab_layout == 'H':
                layout = QHBoxLayout(widget)
                layout.setContentsMargins(1, 1, 1, 1)
                self.tab_dict[tab_text] = [index, widget, layout]
            elif tab_layout == 'G':
                layout = QGridLayout(widget)
                layout.setContentsMargins(1, 1, 1, 1)
                self.tab_dict[tab_text] = [index, widget, layout]

            self.addTab(self.tab_dict[tab_text][1], tab_text)
            return True
        else:
            return False

    def delete_tab(self, tab_text):
        if tab_text not in self.tab_dict:
            index = self.tab_dict[tab_text][0]
            self.removeTab(index)
            self.tab_dict.pop(tab_text)
            for key in self.tab_dict:
                if self.tab_dict[key][0] > index:
                    self.tab_dict[key][0] -= 1

    def getWidgetTab(self, tab_text):
        if tab_text not in self.tab_dict:
            return self.tab_dict[tab_text][1]

    def getTabLayout(self, tab_text):
        if tab_text not in self.tab_dict:
            return self.tab_dict[tab_text][2]