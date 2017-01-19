#PYQT
from PyQt5.QtCore   import pyqtSignal, QSize
from PyQt5.QtGui    import QIcon

from Widgets.PushButton import MYPushButton
from Widgets.Widget     import MYWidget
from icons import ICON


class AcceptRejectButtons(MYWidget):

    #SIGNALS
    clickedAccept = pyqtSignal()
    clickedReject = pyqtSignal()

    def __init__(self, parnt=None):
        super(AcceptRejectButtons, self).__init__(parent=parnt,
                                                  layout='H')
        self.accept = MYPushButton(parent=self)
        self.reject = MYPushButton(parent=self)

        self.main_layout.addWidget(self.accept)
        self.main_layout.addWidget(self.reject)

        self.accept.setToolTip('Accept changes')
        self.reject.setToolTip('Reject changes')

        self.accept.setIcon(QIcon(ICON.SOFTWARES.buttons_accept()))
        self.reject.setIcon(QIcon(ICON.SOFTWARES.buttons_reject()))

        self.accept.setIconSize(QSize(30, 30))
        self.reject.setIconSize(QSize(30, 30))

        self.accept.setFixedSize(30, 30)
        self.reject.setFixedSize(30, 30)

        self.accept.setFlat(True)
        self.reject.setFlat(True)

        self.hideButons()

        #CONNECTS
        self.accept.clicked.connect(self.__EMITT_clickedAccept)
        self.reject.clicked.connect(self.__EMITT_clickedReject)

    def hideButons(self):
        self.accept.hide()
        self.reject.hide()

    def showButons(self):
        self.accept.show()
        self.reject.show()

    def __EMITT_clickedAccept(self):
        self.clickedAccept.emit()
        self.hideButons()

    def __EMITT_clickedReject(self):
        self.clickedReject.emit()
        self.hideButons()


