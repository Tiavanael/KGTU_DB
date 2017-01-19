


#Qt namespace
from PyQt5.QtCore import Qt

#WIDGETS
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QToolBar
from Widgets.Widget  import MYWidget

#PARAMETERS
from parameters import ENABLE_STYLES

#STYLESHEETS
from style import STYLE












class MYMainWindow(QMainWindow):
    def __init__(
            self,
            title=None,
            window_size=(1280, 720),
            cwidget=True,
            layout='V',
            layout_margins=[10, 10, 10, 10],
            spliter=None,
            spliter_margins=[10, 10, 10, 10],
            toolbar=False,
            toolbar_section='Top'
    ):
        super(MYMainWindow, self).__init__()


        #Central widget
        if cwidget:
            self.cwidget = MYWidget(
                parent=self,
                layout=layout,
                layout_margins=layout_margins,
                spliter=spliter,
                spliter_margins=spliter_margins
            )
            self.setCentralWidget(self.cwidget)


        #Tool bar
        if toolbar:
            self.toolbar = QToolBar(self)

            #toolbar section
            if   toolbar_section == 'Top':    tb_section = Qt.TopToolBarArea
            elif toolbar_section == 'Right':  tb_section = Qt.RightToolBarArea
            elif toolbar_section == 'Left':   tb_section = Qt.LeftToolBarArea
            elif toolbar_section == 'Bottom': tb_section = Qt.BottomToolBarArea
            else: tb_section = Qt.TopToolBarArea

            self.addToolBar(tb_section, self.toolbar)


        #PARM
        self.resize(window_size[0], window_size[1])
        self.setWindowTitle(title)

        #STYLING
        if ENABLE_STYLES: self.setStyleSheet(STYLE.Widget)