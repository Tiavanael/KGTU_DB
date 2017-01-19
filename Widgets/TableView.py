

from PyQt5.QtWidgets import QTableView

from parameters      import ENABLE_STYLES
from style import STYLE


class MYTableView(QTableView):
    #INIT
    def __init__(self, parent=None):
        super(MYTableView, self).__init__()

        #PARMS
        if parent: self.setParent(parent)

        self.setAlternatingRowColors(True)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSelectionMode(self.SingleSelection)
        self.setSelectionBehavior(self.SelectRows)
        self.setEditTriggers(self.NoEditTriggers)
        self.setSortingEnabled(True)
        if ENABLE_STYLES: self.setStyleSheet(STYLE.ListWidget)
