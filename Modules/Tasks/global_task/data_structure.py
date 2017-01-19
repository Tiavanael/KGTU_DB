

class GlobalTaskStructure(object):

    def __init__(self):
        super(GlobalTaskStructure, self).__init__()
        self.__name = ''
        self.__descript = ''


    @property
    def name(self):
        return self.__name

    @property
    def task(self):
        return self.__descript

    @property
    def asFieldsForRecord(self):
        return [self.name, self.task]

    def setName(self, name):
        self.__name = str(name)

    def setTask(self, descript):
        self.__descript = str(descript)
