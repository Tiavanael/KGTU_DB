from DataBase.access_model import DBAccessModel
from Modules.Events.BaseClases.data_structure import Structure








class Model(DBAccessModel):
    def __init__(self, data_base):
        super(Model, self).__init__(
            table=DBAccessModel.TableEvents,
            app_db=data_base
        )
        self.setHeaders(
            ['ФИО', 'Место', 'Время', 'Описание', 'Состояние']
        )


    # METHODS
    def getStructure(self, row):
        attrs = self.getRecord(row=row, record_type=self.PyDictRecord)
        struct = Structure(
            fio=attrs['fio'],
            place=attrs['place'],
            db_datetime=attrs['datetime'],
            descript=attrs['descript'],
            state=attrs['state']
        )
        return struct

    def addRecord(self, data_structure, row=0):
        """
        :param data_structure: <ContactStructure> : структура данных
        """
        values = data_structure.asFieldsForRecord
        # print(values)
        super(Model, self).addRecord(fields=values, row=row)

    def editRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        # print(values)
        super(Model, self).editRecord(fields=values, row=row)