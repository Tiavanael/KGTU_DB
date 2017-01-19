# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'notes.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget


class Ui_self(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(640, 480)
        self.calendarFrame = QtWidgets.QGroupBox(self)
        self.calendarFrame.setGeometry(QtCore.QRect(320, 210, 311, 261))
        self.calendarFrame.setObjectName("calendarFrame")
        self.calendar = QtWidgets.QCalendarWidget(self.calendarFrame)
        self.calendar.setGeometry(QtCore.QRect(10, 65, 296, 183))

        self.noteListFrame = QtWidgets.QGroupBox(self)
        self.noteListFrame.setGeometry(QtCore.QRect(10, 0, 311, 471))
        self.noteListFrame.setObjectName("noteListFrame")
        self.noteList = QtWidgets.QTableView(self.noteListFrame)
        self.noteList.setGeometry(QtCore.QRect(10, 20, 291, 410))

        self.calendar.setObjectName("calendar")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.calendarFrame)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 20, 220, 41))
        self.addNoteButton = QPushButton(self.noteListFrame)
        self.addNoteButton.setGeometry(QtCore.QRect(9, 430, 60, 38))
        self.addNoteButton.setText("+")
        self.remNoteButton = QPushButton(self.noteListFrame)
        self.remNoteButton.setGeometry(QtCore.QRect(70, 430, 60, 38))
        self.remNoteButton.setText("-")
        self.showAllButton = QPushButton(self.noteListFrame)
        self.showAllButton.setText("Показать все")
        self.showAllButton.setGeometry(130, 430, 120, 38)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")


        self.noteList.setObjectName("noteList")
        self.noteEditFrame = QtWidgets.QGroupBox(self)
        self.noteEditFrame.setGeometry(QtCore.QRect(320, 0, 311, 211))
        self.noteEditFrame.setObjectName("noteEditFrame")
        self.textEdit = QtWidgets.QTextEdit(self.noteEditFrame)
        self.textEdit.setGeometry(QtCore.QRect(10, 80, 291, 90))
        self.textEdit.setObjectName("textEdit")
        self.themeEdit = QtWidgets.QLineEdit(self.noteEditFrame)
        self.themeEdit.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.themeEdit.setObjectName("themeEdit")
        self.label = QtWidgets.QLabel(self.noteEditFrame)
        self.label.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label.setObjectName("label")

        self.completionEdit = QtWidgets.QComboBox(self.noteEditFrame)
        self.completionEdit.setGeometry(QtCore.QRect(143, 50, 113, 20))
        self.completionEdit.setObjectName("completionEdit")
        self.label_3 = QtWidgets.QLabel(self.noteEditFrame)
        self.label_3.setGeometry(QtCore.QRect(143, 30, 70, 13))
        self.label_3.setObjectName("label_3")

        self.saveButton = QtWidgets.QPushButton(self.noteEditFrame)
        self.saveButton.setGeometry(QtCore.QRect(10, 170, 75, 35))
        self.saveButton.setText("Сохранить")
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle("Календарь")
        self.calendarFrame.setTitle("Календарь/ Время")
        self.noteListFrame.setTitle("Заметки")
        self.noteEditFrame.setTitle("Редактор заметок")
        self.label.setText(" Тема")
        self.label_3.setText("Выполнение")
        self.completionEdit.addItem("Не выполнено")
        self.completionEdit.addItem("В процессе")
        self.completionEdit.addItem("Выполенено")

def getForm():

    form = Ui_self()
    return form


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    self = QtWidgets.QWidget()
    ui = Ui_self()
    ui.setupUi(self)
    self.show()
    sys.exit(app.exec_())

