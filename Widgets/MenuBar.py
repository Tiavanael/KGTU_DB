# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:




from PyQt5.QtWidgets import QMenuBar


class MYMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super(MYMenuBar, self).__init__()
        if parent: self.setParent(parent)