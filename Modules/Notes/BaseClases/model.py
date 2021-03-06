from DataBase.access_model import DBAccessModel
from Modules.Notes.BaseClases.data_structure import Structure





class Model(DBAccessModel):
    def __init__(self, data_base):
        super(Model, self).__init__(
            table=DBAccessModel.TableNotes,
            app_db=data_base
        )
        self.setHeaders(['Тема', 'Описание', 'Дата'])
    def getStructure(self, row):
        attrs = self.getRecord(row=row, record_type=self.PyDictRecord)
        struct = Structure(
            theme=attrs['theme'],
            description=attrs['descript'],
            db_datetime=attrs['datetime']
        )
        return struct

    def addRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(Model, self).addRecord(fields=values, row=row)

    def editRecord(self, data_structure, row):
        values = data_structure.asFieldsForRecord
        super(Model, self).editRecord(row=row, fields=values)
