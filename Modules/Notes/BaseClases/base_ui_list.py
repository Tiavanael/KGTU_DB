from Widgets.TableView import MYTableView





class BaseUIList(MYTableView):
    # SIGNALS



    def __init__(self, model, parent=None):
        super(BaseUIList, self).__init__(parent=parent)

        self.__init_Parameters(model)




    def __init_Parameters(self, model):
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.SingleSelection)
        self.setModel(model)
        self.hideColumn(1)
        self.setColumnWidth(0, 370)
        # self.hideColumn(2)




