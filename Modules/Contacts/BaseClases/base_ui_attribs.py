
# Qt Types

from Modules.Contacts.BaseClases.data_structure import Structure

# WIDGETS
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QHBoxLayout
from Widgets.LineEdit import MYLineEdit
from Widgets.Label import MYLabel
from Widgets.Widget import MYWidget
from Widgets.ComboBox import MYComboBox

from PyQt5.QtGui     import QDoubleValidator








class BaseUIAttribs(MYWidget):
    """
    Базовый класс, обеспечивающий GUI
    для атрибутов "Заметки".
    """

    # роль
    Editable = 0
    NotEditable = 1

    def __init__(self, role=Editable, parent=None):
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

        self.__init_Attributes(role)
        self.__init_Parameters()
        self.__init_Layouting()




    # inits
    def __init_Attributes(self, role):
        self.__structure = Structure()

        self.__uitype = role

        self.btns_layout = QHBoxLayout()
        self.__form_layout = QFormLayout()

        self.__lbl_fio   = MYLabel(parent=self, bold=True, text='ФИО:')
        self.__lbl_phone = MYLabel(parent=self, bold=True, text='Телефон:')
        self.__lbl_group = MYLabel(parent=self, bold=True, text='Группа:')
        self.__lbl_comp  = MYLabel(parent=self, bold=True, text='Фирма:')

        if self.__uitype == self.Editable:
            self.__fio   = MYLineEdit(parent=self)
            self.__phone = MYLineEdit(self)
            self.__group = MYComboBox(parent=self)
            self.__comp = MYLineEdit(parent=self)
        else:
            self.__fio   = MYLabel(parent=self, bold=False, italic=True)
            self.__phone = MYLabel(parent=self, bold=False, italic=True)
            self.__group = MYLabel(parent=self, bold=False, italic=True)
            self.__comp = MYLabel(parent=self, bold=False, italic=True)

    def __init_Parameters(self):
        self.__form_layout.setContentsMargins(0, 0, 0, 0)
        self.__form_layout.setSpacing(5)

        if self.__uitype == self.Editable:
            self.__group.addItem('Работа')
            self.__group.addItem('Личное')
            validator = QDoubleValidator(0, 15, 2, self)
            # mask = '00000000000'
            self.__phone.setValidator(validator)
            self.__phone.setMaxLength(11)
            # self.__phone.setInputMask(mask)

    def __init_Layouting(self):

        AS_FIELD = self.__form_layout.FieldRole
        AS_LABEL = self.__form_layout.LabelRole

        self.main_layout.addLayout(self.__form_layout)
        self.main_layout.addLayout(self.btns_layout)

        self.__form_layout.setWidget(0, AS_LABEL, self.__lbl_fio)
        self.__form_layout.setWidget(1, AS_LABEL, self.__lbl_phone)
        self.__form_layout.setWidget(2, AS_LABEL, self.__lbl_group)
        self.__form_layout.setWidget(3, AS_LABEL, self.__lbl_comp)

        self.__form_layout.setWidget(0, AS_FIELD, self.__fio)
        self.__form_layout.setWidget(1, AS_FIELD, self.__phone)
        self.__form_layout.setWidget(2, AS_FIELD, self.__group)
        self.__form_layout.setWidget(3, AS_FIELD, self.__comp)




    @property
    def dataStructure(self):
        self.__structure.setFIO(self.__fio.text())
        self.__structure.setPhone(self.__phone.text())
        self.__structure.setCompany(self.__comp.text())
        if self.__uitype == self.Editable:
            self.__structure.setGroup(self.__group.currentText())
        else:
            self.__structure.setGroup(self.__group.text())
        return self.__structure


    # METHODS
    def setDataStructure(self, struct):
        self.__structure = struct

        self.__fio.setText(struct.FIO)
        self.__phone.setText(struct.phone)
        self.__comp.setText(struct.company)

        if self.__uitype == self.Editable:
            self.__group.setCurrentText(struct.group)
        else:
            self.__group.setText(struct.group)











if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])

    struct = Structure(
        fio='Григорян Олегсей Костикович',
        phone='891148897',
        group='Личное'
    )

    win = BaseUIAttribs(BaseUIAttribs.NotEditable)
    win.setDataStructure(struct)

    win.show()
    app.exec_()
