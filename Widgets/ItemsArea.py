# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:




from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

from Widgets.ScrollArea import MYScrollArea
from Widgets.Spacer     import MYSpacer
from parameters         import ENABLE_STYLES
from style import STYLE


class MYItem(QVBoxLayout):

    #SIGNALS
    destructed = pyqtSignal(str)

    #INIT
    def __init__(self,
                 item_name,
                 contnt):
        super(MYItem, self).__init__()
        self.name = item_name

        #CONTANTING
        self.content = contnt
        try: self.addWidget(self.content)
        except: self.addLayout(self.content)

    #METHODES
    def getContenAttribs(self):
        return self.content.transmitContentAttribs()

    #DESTRUCTOR
    def destruct(self):
        self.content.setParent(None)
        self.content.destroy()
        self.deleteLater()
        self.destructed.emit(self.name)


class MYItemsArea(MYScrollArea):

    #SIGNALs
    SIGNAL_itemAdded   = pyqtSignal(str)
    SIGNAL_itemRemoved = pyqtSignal(str)

    #INIT
    def __init__(self, parent=None):
        super(MYItemsArea, self).__init__(layout='V',
                                          layout_spacing=5,
                                          layout_margins=[5, 5, 5, 5],
                                          )
        if parent: self.setParent(parent)
        self.items = {}
        self.spacer = MYSpacer()

        #STYLE
        if ENABLE_STYLES: self.setStyleSheet(STYLE.ScrollArea)

        #LAYOUTING
        self.content_widget.main_layout.addItem(self.spacer)

        #CONNECTS

    #SLOTS
    def addItem(self, name, item_content):
        name = str(name)
        if name not in self.items:
            self.content_widget.main_layout.removeItem(self.spacer)
            self.items[name] = MYItem(contnt=item_content,
                                      item_name=name
                                      )
            self.content_widget.main_layout.addLayout(self.items[name])
            self.content_widget.main_layout.addItem(self.spacer)
            self.SIGNAL_itemAdded.emit(name)

    def removeItem(self, name):
        name = str(name)
        if name in self.items:
            self.items[name].destruct()
            self.items.pop(name)
            self.SIGNAL_itemRemoved.emit(name)

    def getItemsContentValues(self):
        values = {}
        for name in self.items:
            values[name] = self.items[name].getContentValues()
        return values

    def getItemContentValues(self, item_name):
        return self.items[item_name].getContentValues()









class Fortesting(QWidget):
    def __init__(self):
        super(Fortesting, self).__init__()
        self.main_laiyout = QVBoxLayout(self)
        self.line = QLineEdit('12345', self)
        self.btn = QPushButton('ADD', self)
        self.btn_del = QPushButton('Del', self)
        self.area = MYItemsArea(self)


        self.main_laiyout.addWidget(self.area)
        self.main_laiyout.addWidget(self.line)
        self.main_laiyout.addWidget(self.btn)
        self.main_laiyout.addWidget(self.btn_del)

        self.btn.clicked.connect(self.add)
        self.btn_del.clicked.connect(self.remv)

    def add(self):
        for i in self.line.text():
            label = QLabel(i)
            label.setFixedHeight(80)
            self.area.addItem(i, label)

    def remv(self):
        self.area.removeItem(self.line.text())


if __name__ == '__main__':
    app = QApplication([])
    win = Fortesting()
    win.show()
    app.exec_()