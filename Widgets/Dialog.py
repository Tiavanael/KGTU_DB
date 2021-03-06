
#PYQt
from PyQt5.QtCore import Qt
from PyQt5.QtGui  import QIcon
from PyQt5.QtWidgets    import QDialog
from PyQt5.QtWidgets    import QGridLayout
from PyQt5.QtWidgets    import QHBoxLayout
from PyQt5.QtWidgets    import QSplitter
from PyQt5.QtWidgets    import QVBoxLayout

from Widgets.PushButton import MYPushButton
from Widgets.Spacer     import MYSpacer
from icons import ICON
from parameters import ENABLE_STYLES
from style import STYLE


class MYDialog(QDialog):
    def __init__(
            self,
            parent=None,
            title=None,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=5,
            spliter=None,
            spliter_margins=[0, 0, 0, 0],
            CLOSE_btn_name='Close',
            OK_btn_name='OK',
            btn_spacer=True
    ):
        super(MYDialog, self).__init__()

        if parent: self.setParent(parent, Qt.Window)

        if title: self.setWindowTitle(str(title))

        self.dialog_layout = QVBoxLayout(self)

        if layout == 'V':
            self.main_layout = QVBoxLayout()
            self.main_spacer = MYSpacer('V')
        elif layout == 'H':
            self.main_layout = QHBoxLayout()
            self.main_spacer = MYSpacer('H')
        elif layout == 'G':
            self.main_layout            = QGridLayout()
            self.main_spacer_vertical   = MYSpacer('V')
            self.main_spacer_horizontal = MYSpacer('H')


        self.main_layout.setSpacing(layout_spacing)
        self.main_layout.setContentsMargins(
            layout_margins[0],
            layout_margins[1],
            layout_margins[2],
            layout_margins[3]
        )


        if layout == 'V' or layout == 'H':
            if spliter:

                if   spliter == 'V': self.main_spliter = QSplitter(Qt.Vertical)
                elif spliter == 'H': self.main_spliter = QSplitter(Qt.Horizontal)

                self.main_spliter.setContentsMargins(
                    spliter_margins[0],
                    spliter_margins[1],
                    spliter_margins[2],
                    spliter_margins[3]
                )
                self.main_layout.addWidget(self.main_spliter)


        if ENABLE_STYLES: self.setStyleSheet(STYLE.Widget)




        #ATTRIBUTES
        self.btn_layout = QHBoxLayout()
        self.close_btn  = MYPushButton(parent=self, text=CLOSE_btn_name)
        self.ok_btn     = MYPushButton(parent=self, text=OK_btn_name)

        #PARMS
        self.close_btn.setIcon(QIcon(ICON.DEFAULT.cancel()))
        self.ok_btn.setIcon(QIcon(ICON.DEFAULT.OK()))

        #LAYOUTING
        if btn_spacer: self.btn_layout.addItem(MYSpacer('H'))
        self.btn_layout.addWidget(self.ok_btn)
        self.btn_layout.addWidget(self.close_btn)
        #self.dialog_layout.addItem(MYSpacer())
        self.dialog_layout.addLayout(self.main_layout)
        self.dialog_layout.addLayout(self.btn_layout)

        self.ok_btn.setFixedWidth(100)
        self.close_btn.setFixedWidth(100)


        #CONNECTS
        self.close_btn.clicked.connect(self.reject)
        self.ok_btn.clicked.connect(self.accept)







if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    win = MYDialog()
    win.exec_()
    app.exec_()