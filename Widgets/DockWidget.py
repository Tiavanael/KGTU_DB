# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:

from PyQt5.QtCore    import Qt
from PyQt5.QtWidgets import QDockWidget

from parameters      import ENABLE_STYLES
from style import STYLE


class MYDockWidget(QDockWidget):
    def __init__(self,
                 parent=None,
                 title=None,
                 content=None,
                 floating=True,
                 movable=True
                 ):
        super(MYDockWidget, self).__init__()
        #PARMS
        if parent: self.setParent(parent)
        if title: self.setWindowTitle(title)
        if content: self.setWidget(content)
        if movable: self.setFeatures(QDockWidget.DockWidgetMovable)
        if floating: self.setFloating(True)
        self.setAllowedAreas(Qt.AllDockWidgetAreas)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.DockWidget)

    def addContent(self, content):
        self.setWidget(content)

    def removeContent(self):
        self.content.children().setParent(None)