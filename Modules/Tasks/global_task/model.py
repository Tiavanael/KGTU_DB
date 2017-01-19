from DataBase.access_model import DBAccessModel
from Modules.Tasks.global_task.data_structure import GlobalTaskStructure as Structure






class ModelGlob(DBAccessModel):
    def __init__(self, data_base):
        super(ModelGlob, self).__init__(
            table=DBAccessModel.TableTasks,
            app_db=data_base
        )
        self.setHeaders(
            ['Название', 'Описание']
        )


    # METHODS
    def getStructure(self, row):
        attrs = self.getRecord(row=row, record_type=self.PyDictRecord)
        data = Structure()
        data.setName(attrs['name'])
        data.setTask(attrs['descript'])
        return data

    def addRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(ModelGlob, self).addRecord(fields=values, row=row)

    def editRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(ModelGlob, self).editRecord(fields=values, row=row)