from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QColor

from DataBase.access_model import DBAccessModel
from Modules.Tasks.BaseClases.data_structure import Structure





class ModelDep(DBAccessModel):
    def __init__(self, data_base):
        super(ModelDep, self).__init__(
            table=DBAccessModel.TableDepartments,
            app_db=data_base
        )




class ModelDepTask(DBAccessModel):
    def __init__(self, data_base):
        super(ModelDepTask, self).__init__(
            table=DBAccessModel.TableDepartmentTasks,
            app_db=data_base
        )
        self.setHeaders(
            ['Отдел', 'Поручение', 'Дата начала', 'Дата отчета', 'Состояние']
        )


    # METHODS
    def getStructure(self, row):
        attrs = self.getRecord(row=row, record_type=self.PyDictRecord)
        data = Structure()
        data.setName(attrs['name'])
        data.setTask(attrs['task'])
        data.setDBDateTimeStart(attrs['datetime_start'])
        data.setDBDateTimeFinish(attrs['datetime_finish'])
        data.setState(attrs['state'])

        return data

    def addRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(ModelDepTask, self).addRecord(fields=values, row=row)

    def editRecord(self, data_structure, row=0):
        values = data_structure.asFieldsForRecord
        super(ModelDepTask, self).editRecord(fields=values, row=row)


    def data(self, index, role=Qt.BackgroundRole):
        if role == Qt.ForegroundRole:
            row = index.row()
            col = index.column()
            if col == 0:
                data = self.getStructure(row)
                date_f = data.qDateTimeFinish
                state = data.state
                if state == 1:
                    brush = QBrush()
                    color = QColor(0, 255, 0, 200)
                    brush.setColor(color)
                    return brush
                elif date_f.currentDateTime() < date_f:
                    brush = QBrush()
                    color = QColor(255, 255, 0, 200)
                    brush.setColor(color)
                    return brush
                elif (date_f.currentDateTime() >= date_f) or (state == 0):
                    brush = QBrush()
                    color = QColor(255, 0, 0, 200)
                    brush.setColor(color)
                    return brush
        else:
            return super(ModelDepTask, self).data(index, role)