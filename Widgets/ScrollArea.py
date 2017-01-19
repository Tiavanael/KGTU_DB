# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:





from PyQt5.QtWidgets import QScrollArea

from Widgets.Widget  import MYWidget
from parameters      import ENABLE_STYLES
from style import STYLE


class MYScrollArea(QScrollArea):
    def __init__(self,
                 parent=None,
                 layout='V',
                 layout_margins=[0, 0, 0, 0],
                 layout_spacing=5,
                 spliter=None,
                 spliter_margins=[0, 0, 0, 0]
                 ):
        super(MYScrollArea, self).__init__()

        if parent: self.setParent(parent)

        self.content_widget = MYWidget(parent=None,
                                       layout=layout,
                                       layout_margins=layout_margins,
                                       layout_spacing=layout_spacing,
                                       spliter=spliter,
                                       spliter_margins=spliter_margins)
        self.setWidget(self.content_widget)
        self.setWidgetResizable(True)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.ScrollArea)



    def addContent(self, widget):
        widget.setParent(self.content_widget)
        self.content_widget.main_layout.addWidget(widget)



# class Fortesting(QWidget):
#     def __init__(self):
#         super(Fortesting, self).__init__()
#         self.main_laiyout = QVBoxLayout(self)
#         self.line = QLineEdit('12345', self)
#         self.btn = QPushButton('ADD', self)
#         self.area = MYScrollArea(self)
#
#
#         self.main_laiyout.addWidget(self.area)
#         self.main_laiyout.addWidget(self.line)
#         self.main_laiyout.addWidget(self.btn)
#
#         self.btn.clicked.connect(self.add)
#
#
#     def add(self):
#         for i in self.line.name():
#             label = QLabel(i)
#             self.area.addContent(label)
#
# if __name__ == '__main__':
#     app = QApplication([])
#     win = Fortesting()
#     win.show()
#     app.exec_()