from DataBase.access_model import DBAccessModel
from Modules.Contacts.BaseClases.data_structure import Structure





class Model(DBAccessModel):
    def __init__(self, data_base):
        super(Model, self).__init__(
            table=DBAccessModel.TableContacts,
            app_db=data_base
        )
        self.setHeaders(["ФИО", 'НОМЕР', 'ГРУППА', 'ФИРМА'])

    def getStructure(self, row):
        attrs = self.getRecord(row=row, record_type=self.PyDictRecord)
        struct = Structure(
            fio = attrs['name'],
            phone=attrs['phone'],
            group=attrs['group'],
            company=attrs['company']
        )
        return struct

    def addRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(Model, self).addRecord(fields=values, row=row)

    def editRecord(self, data_structure, row):
        values = data_structure.asFieldsForRecord
        super(Model, self).editRecord(row=row, fields=values)
