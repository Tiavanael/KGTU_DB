# Qt Types

from Modules.Emloyees.BaseClases.data_structure import Structure
from DataBase.access_model import DBAccessModel

# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from Widgets.LineEdit import MYLineEdit
from Widgets.ComboBox import MYComboBox
from Widgets.Label import MYLabel
from Widgets.Widget import MYWidget
from PyQt5.QtWidgets import QSpinBox







class BaseUIAttribs(MYWidget):
    """
    Базовый класс, обеспечивающий GUI
    для атрибутов "Сотрудника".
    """

    # роль
    Editable = 0
    NotEditable = 1

    def __init__(self, DB, role=Editable, parent=None):
        """
        Параметр role должен принимать одно из
        двух значений:
            - Editable    - редактируемый GUI
            - NotEditable - не редактируемый GUI

        :param role: <BaseUIAttribs.Editable, BaseUIAttribs.NotEditable>
        :param parent: <QtWidget> : Qt родитель
        """



        super(BaseUIAttribs, self).__init__(
            parent=parent,
            layout='V',
            layout_margins=[0, 0, 0, 0],
            layout_spacing=10
        )

        self.__uitype = role
        self.__structure = Structure()

        if self.__uitype == self.Editable:
            self.__init_EditableAttributes(DB=DB)
        else:
            self.__init_NotEditableAttributes()

        self.__init_Parameters()
        self.__init_Layouting()




    # inits
    def __init_EditableAttributes(self, DB):
        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__department_model = DBAccessModel(
            table=DBAccessModel.TableDepartments,
            app_db=DB,
            parent=self
        )

        self.__lbl_fio = MYLabel(parent=self, bold=True, text='ФИО:')
        self.__lbl_salary  = MYLabel(parent=self, bold=True, text='Зарплата:')
        self.__lbl_department = MYLabel(parent=self, bold=True, text='Отдел:')
        self.__lbl_post = MYLabel(parent=self, bold=True, text='Должность:')

        self.__fio = MYLineEdit(parent=self)
        self.__salary = QSpinBox(self)
        self.__department = MYComboBox(parent=self)
        self.__post = MYComboBox(parent=self)

    def __init_NotEditableAttributes(self):
        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_fio = MYLabel(parent=self, bold=True, text='ФИО:')
        self.__lbl_salary = MYLabel(parent=self, bold=True, text='Зарплата:')
        self.__lbl_department = MYLabel(parent=self, bold=True, text='Отдел:')
        self.__lbl_post = MYLabel(parent=self, bold=True, text='Должность:')

        self.__fio = MYLabel(parent=self, bold=False, italic=True)
        self.__salary = MYLabel(parent=self, bold=False, italic=True)
        self.__department = MYLabel(parent=self, bold=False, italic=True)
        self.__post = MYLabel(parent=self, bold=False, italic=True)

    def __init_Parameters(self):
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

        if self.__uitype == self.Editable:
            self.__salary.setMaximum(1000000000)
            self.__department.setModel(self.__department_model)
            self.__post.addItems([
                'Главный проектировщик',
                'Главный дизайнер',
                'Главный программист',
                'UIX',
                'Системный инженер',
                'Тестировщик'
            ])

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addLayout(self.btns_layout)

        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_fio)
        self.__form_layout.setWidget(1, AS_LABEL, self.__lbl_salary)
        self.__form_layout.setWidget(2, AS_LABEL, self.__lbl_department)
        self.__form_layout.setWidget(3, AS_LABEL, self.__lbl_post)

        self.__form_layout.setWidget(0, AS_FIELD, self.__fio)
        self.__form_layout.setWidget(1, AS_FIELD, self.__salary)
        self.__form_layout.setWidget(2, AS_FIELD, self.__department)
        self.__form_layout.setWidget(3, AS_FIELD, self.__post)




    @property
    def dataStructure(self):
        fio = self.__fio.text()
        salary = self.__salary.text()

        if self.__uitype == self.Editable:
            department = self.__department.currentText()
            post = self.__post.currentText()
        else:
            department = self.__department.text()
            post = self.__post.text()

        self.__structure.setFIO(fio)
        self.__structure.setSalary(salary)
        self.__structure.setDepartment(department)
        self.__structure.setPost(post)

        return self.__structure


    # METHODS
    def setDataStructure(self, struct):
        self.__structure = struct

        self.__fio.setText(struct.FIO)

        if self.__uitype == self.Editable:
            self.__salary.setValue(struct.salary)
            self.__department.setCurrentText(struct.department)
            self.__post.setCurrentText(struct.post)
        else:
            self.__salary.setText(str(struct.salary))
            self.__department.setText(struct.department)
            self.__post.setText(struct.post)

