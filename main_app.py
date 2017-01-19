import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase

from Utility.ReportClass import Report
from paths import DB_FILE_PATH
from Utility.messages import MESSAGE

# МОДУЛИ
from Modules.Main_Window.Window.main import AppMainWindow



style = """

QTableView QTableCornerButton::section
{
      border: 1px solid rgb(99, 99, 99);
      background-color: rgb(58, 58, 58);
}

QWidget
{
    font-family: "DejaVu Sans";
    font-size: 11px;
    color: rgb(204, 204, 204);
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(58, 58, 58),
				stop: 1.0 rgb(58, 58, 58));
}

QWidget[transparent="true"]
{
    background: black;
    border: none;
}

QWidget:disabled
{
    color: rgb(131, 131, 131);
}

.QWidget
{
    background-color: rgb(58, 58, 58);
}

ExampleHelpWidget[help_text="true"]
{
    border-bottom: 1px solid rgb(204, 204, 204);
}

CaptureWidget
{
    background-color: #FF0000;
    border-bottom: 1px solid rgb(204, 204, 204);
}

QDialog, QFrame, QGroupBox
{
    background: rgb(58, 58, 58);
    color: rgb(204, 204, 204);
}


QGroupBox
{
    border: 1px solid rgb(28, 28, 28);
    border-radius: 5px;
}

QGroupBox::title
{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    background: none;
    padding: 0 3px;
    position: absolute;
    left: 10px;
}

#central_widget
{
    background: rgb(58, 58, 58);
    color: rgb(204, 204, 204);
}


QTextEdit
{
    background: rgb(77, 77, 77);
    color: rgb(204, 204, 204);
    selection-background-color: rgb(184, 134, 32);
    selection-color: rgb(0, 0, 0);
    border: 1px solid rgb(99, 99, 99);
}

QTextEdit#code_edit
{
    background: rgb(86, 86, 86);
    font-size: 15px;
    border: 1px solid rgb(99, 99, 99);
}

QTextBrowser
{
    background: rgba(255, 255, 255, 0);
    color: rgb(204, 204, 204);
    selection-background-color: rgb(184, 134, 32);
    selection-color: rgb(0, 0, 0);
    border: 1px solid rgb(99, 99, 99);
}

QCheckBox
{
    background: rgb(58, 58, 58);
}

QCheckBox:disabled
{
    color: rgb(131, 131, 131);
}

QDateEdit
{
    border: 1px solid rgba(0, 0, 0, 102);
    border-radius: 1px;
    padding-top: 2px;
    padding-bottom: 2px;
    padding-right: 2px;
    padding-left: 2px;
    background: qlineargradient(x1: 0, y1: 0,x2: 0, y2: 1,
                                stop: 0.0 rgb(86, 86, 86),
                                stop: 1.0 rgb(58, 58, 58));
}

QDateEdit:disabled
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0.0 rgba(86, 86, 86, 40),
				    stop: 1.0 rgba(58, 58, 58, 40));
    color: rgb(131, 131, 131);
}

QDateEdit::drop-down
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(63, 63, 63),
				stop: 1.0 rgb(38, 38, 38));
    width: 20px;
}

QDateEdit::down-arrow
{
    width: 0;
    height: 0;
    border-left: 3px solid rgba(63, 63, 63, 0);
    border-right: 3px solid rgba(63, 63, 63, 0);
    border-top: 5px solid rgb(131, 131, 131);
}

QComboBox
{
    border: 1px solid rgba(0, 0, 0, 102);
    border-radius: 1px;
    padding-top: 2px;
    padding-bottom: 2px;
    padding-right: 2px;
    padding-left: 2px;
    background: qlineargradient(x1: 0, y1: 0,x2: 0, y2: 1,
                                stop: 0.0 rgb(86, 86, 86),
                                stop: 1.0 rgb(58, 58, 58));
}

QComboBox:disabled
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                    stop: 0.0 rgba(86, 86, 86, 40),
				    stop: 1.0 rgba(58, 58, 58, 40));
    color: rgb(131, 131, 131);
}

QComboBox::drop-down
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(63, 63, 63),
				stop: 1.0 rgb(38, 38, 38));
    width: 20px;
}

QComboBox::down-arrow
{
    width: 0;
    height: 0;
    border-left: 3px solid rgba(63, 63, 63, 0);
    border-right: 3px solid rgba(63, 63, 63, 0);
    border-top: 5px solid rgb(131, 131, 131);
}

QComboBox QAbstractItemView
{
    background-color: rgb(58, 58, 58);
    border-top: 1px solid rgb(58, 58, 58);
    border-left: 1px solid rgb(58, 58, 58);
    border-bottom: 1px solid rgb(204, 204, 204);
    border-right: 1px solid rgb(204, 204, 204);
    padding: 0px;
    selection-background-color: rgb(178, 102, 0);
}

QComboBox QAbstractItemView::item
{
    padding: 4px 15px 4px 15px;
}

QComboBox QAbstractItemView::item:selected
{
    background-color: rgb(178, 102, 0);
    color: rgb(255, 255, 255);
}

QSplitter::handle:horizontal
{
    background-color: rgb(102, 102, 102);
    width: 4px;
}

QSplitter::handle:vertical
{
    background-color: rgb(102, 102, 102);
    height: 4px;
}

QSplitter::handle:pressed
{
    background-color: rgb(184, 134, 32);
}

QSplitter::handle:hover
{
    background-color: rgb(184, 134, 32);
}

QLineEdit, QSpinBox, QTimeEdit
{
    border: 1px solid rgb(35, 35, 35);
    border-radius: 5px;
    padding: 4px 4px 4px 4px;
    background: rgb(77, 77, 77);
    selection-color: rgb(0, 0, 0);
    selection-background-color: rgb(184, 134, 32);
}

QLineEdit:disabled, QSpinBox:disabled
{
    border: 1px solid rgba(35, 35, 35, 40);
    border-radius: 1px;
    padding: 1px 1px;
    background: rgba(19, 19, 19, 40);
    color: rgb(131, 131, 131);
}

QLineEdit[invalid="true"], QSpinBox[invalid="true"]
{
    background: rgb(242, 142, 142);
}

QSpinBox::up-arrow, QTimeEdit::up-arrow{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(63, 63, 63),
				stop: 1.0 rgb(38, 38, 38));
    width: 0;
    height: 0;
    border-left: 6px solid rgba(86, 86, 86, 0);
    border-right: 6px solid rgba(86, 86, 86, 0);
    border-bottom: 6px solid rgb(131, 131, 131);
}

QSpinBox::down-arrow, QTimeEdit::down-arrow {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(63, 63, 63),
				stop: 1.0 rgb(38, 38, 38));
    width: 0;
    height: 0;
    border-left: 6px solid rgba(86, 86, 86, 0);
    border-right: 6px solid rgba(86, 86, 86, 0);
    border-top: 6px solid rgb(131, 131, 131);
}


QLabel:enabled
{
    color: rgb(204, 204, 204);
}

QLabel:disabled
{
    color: rgb(131, 131, 131);
}

#big_text
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
    font-size: 16px;
    font-weight: bold;
    padding: 10px;
    border: none;
    border-bottom: 2px solid rgb(102, 102, 102);
    height: 20px;
    margin-left: -1px;
}

QPushButton:hover#big_text
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(90, 90, 90),
				stop: 1.0 rgb(61, 61, 61));
}

QPushButton:pressed#big_text
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(184, 134, 32),
				stop: 1.0 rgb(184, 134, 32));
    color: rgb(255, 255, 255);
}

QPushButton
{
    border: 1px solid rgb(90, 90, 90);
    border-radius: 4px;
    padding-top: 4px;
    padding-bottom: 4px;
    padding-right: 4px;
    padding-left: 4px;
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
}

GridEntry
{
    outline: none;
}

GridEntry:hover
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(94, 94, 94),
				stop: 1.0 rgb(64, 64, 64));
}

QRadioButton
{
    background: rgb(58, 58, 58);
    color: rgb(203, 203, 203);
    padding: 4px;
}

QRadioButton:disabled
{
    color: rgb(131, 131, 131);
}

QToolButton
{
    border: 1px solid rgb(0, 0, 0);
    border-radius: 4px;
    padding-top: 2px;
    padding-bottom: 2px;
    padding-right: 2px;
    padding-left: 2px;
    margin: 1px;
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
}

QCommandLinkButton#online_login_button,
QCommandLinkButton#traditional_login_button
{
    border: none;
    background: none;
}

QCommandLinkButton#online_login_button:hover,
QCommandLinkButton#traditional_login_button:hover
{
    background: rgb(90, 90, 90);
}

QPushButton:hover, QToolButton:hover
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(90, 90, 90),
				stop: 1.0 rgb(61, 61, 61));
}

QPushButton:pressed, QToolButton:pressed
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(184, 134, 32),
				stop: 1.0 rgb(184, 134, 32));
    color: rgb(255, 255, 255);
}

QPushButton:checked, QToolButton:checked
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(138, 100, 24),
				stop: 1.0 rgb(138, 100, 24));
    color: rgb(255, 255, 255);
}

QPushButton:disabled, QToolButton:disabled
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgba(86, 86, 86, 40),
				stop: 1.0 rgba(58, 58, 58, 40));
    color: rgb(131, 131, 131);
}

QPushButton:flat, QToolButton:flat
{
      border: none;
      background: rgb(58, 58, 58);
}

QPushButton[actionButton="true"]
{
    border-width: 1px;
    border-radius: 2px;
    padding-left: 15px;
    padding-right: 15px;
}

QToolButton[plain="true"], QToolButton[transparent="true"]
{
    background: none;
    border: none;
}

QToolButton[transparent="true"]:hover
{
    background:black;
    border: outset 1px;
}

QToolButton[plain="true"]:hover
{
    background: none;
    border: none;
}

QToolButton[transparent="true"]:pressed
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(184, 134, 32),
				stop: 1.0 rgb(184, 134, 32));
    color: rgb(255, 255, 255);
}

QToolButton[transparent="true"]:disabled
{
    background: none;
    border: none;
}

QListView
{
    alternate-background-color: rgb(58, 58, 58);
    background: rgb(45, 45, 45);
    selection-background-color: rgba(184, 134, 32, 77);
    selection-color: rgb(0, 0, 0);
    color: rgb(204, 204, 204);
}

QListView::item
{
    border-right: 1px solid rgb(25, 25, 25);
    border-left: 0;
    border-top: 0;
    border-bottom: 0;
}

QListView::item:selected
{
    border-top: 1px solid rgb(184, 134, 32);
    border-bottom: 1px solid rgb(184, 134, 32);
    color: rgb(204, 204, 204);
    background: rgba(184, 134, 32, 77);
}

QTableView
{
    alternate-background-color: rgb(58, 58, 58);
    background: rgb(45, 45, 45);
    selection-background-color: rgba(184, 134, 32, 77);
    selection-color: rgb(0, 0, 0);
    color: rgb(204, 204, 204);

}

QTableView::item
{
    border-right: 1px solid rgb(25, 25, 25);
    border-left: 0;
    border-top: 0;
    border-bottom: 0;

}

QTableView::item:selected
{
    color: rgb(204, 204, 204);
    background: rgba(184, 134, 32, 77);
}

QTreeView
{
    alternate-background-color: rgb(58, 58, 58);
    background: rgb(45, 45, 45);
    selection-background-color: rgba(184, 134, 32, 77);
    selection-color: rgb(0, 0, 0);
    color: rgb(204, 204, 204);
}

QTreeView::item
{
    border-right: 1px solid rgb(25, 25, 25);
    border-left: 0;
    border-top: 0;
    border-bottom: 0;
}

QTreeView::item:selected
{
    color: rgb(204, 204, 204);
    background: rgba(184, 134, 32, 77);
}

QHeaderView::section
{
    font: bold;
    border: 1px solid rgb(25, 25, 25);
    border-right: 0;
    padding: 4px;
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(58, 58, 58),
				stop: 1.0 rgb(38, 38, 38) );
}

QTabWidget
{
    background: rgb(58, 58, 58);
    border: 1px solid rgb(99, 99, 99);
}

QTabBar
{
    background: rgb(58, 58, 58);
    border: 1px solid rgb(99, 99, 99);
}


QTabWidget::pane
{
    border: 1px solid solid rgb(99, 99, 99);
    background: rgb(58, 58, 58);
}

QTabWidget::tab-bar
{
    alignment: left;
    left: 1px;
    border: 1px solid rgb(99, 99, 99);
    background: rgb(58, 58, 58);
}

QTabBar::tab
{
    padding-left: 6px;
    padding-right: 6px;
    height: 24px;
    margin-top: 1px;
    margin-left: -1px;
    border: 1px solid rgb(99, 99, 99);
    border-radius: 0px;
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(45, 45, 45));
}

QTabBar[webbrowser="true"]::tab
{
    width: 100px;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
    border: 1px solid rgb(99, 99, 99);
}

QTabBar[webbrowser="true"]::tab:last
{
    border-color: rgb(58, 58, 58);
    border-radius: 0px;
    background: none;
}

QTabBar::tab:selected
{

    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(106, 106, 106),
				stop: 1.0 rgb(78, 78, 78));
}

QTabBar[webbrowser="true"]::close-button
{
    subcontrol-position: right;
    image: url(:/BUTTONS/delete.svg);
    width: 8px;
    height: 8px;
    margin: 4px;
}

QMenu
{
    background-color: rgb(58, 58, 58);
    border-top: 1px solid rgb(147, 147, 147);
    border-left: 1px solid rgb(147, 147, 147);
    border-bottom: 1px solid rgb(38, 38, 38);
    border-right: 1px solid rgb(38, 38, 38);
    padding: 0px;
    font-size: 12px;
}



QScrollBar:horizontal
{
    border: 1px solid rgb(45, 45, 45);
    background: rgb(38, 38, 38);
    height: 15px;
    margin: 0 17px 0 17px;
}

QScrollBar::handle:horizontal
{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
    min-width: 30px;
}

QScrollBar::add-line:horizontal
{
    border: 1px solid rgb(73, 73, 73);

    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
    width: 15px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    border: 1px solid rgb(127, 127, 127);

    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
    width: 15px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::left-arrow:horizontal
{
    width: 0;
    height: 0;
    border-top: 3px solid rgb(86, 86, 86);
    border-bottom: 3px solid rgb(86, 86, 86);
    border-right: 5px solid rgb(131, 131, 131);
}

QScrollBar::right-arrow:horizontal
{
    width: 0;
    height: 0;
    border-top: 3px solid rgb(86, 86, 86);
    border-bottom: 3px solid rgb(86, 86, 86);
    border-left: 5px solid rgb(131, 131, 131);
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    border: 1px solid rgb(45, 45, 45);
    background: rgb(38, 38, 38);
    width: 15px;
    margin: 17px 0 17px 0;
}

QScrollBar::handle:vertical
{
    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
    min-height: 30px;
}

QScrollBar::add-line:vertical
{
    border: 1px solid rgb(127, 127, 127);

    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
    height: 15px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical
{
    border: 1px solid rgb(127, 127, 127);

    background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
				stop: 0.0 rgb(86, 86, 86),
				stop: 1.0 rgb(58, 58, 58));
    height: 15px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical
{
    width: 0;
    height: 0;
    border-left: 3px solid rgba(86, 86, 86, 0);
    border-right: 3px solid rgba(86, 86, 86, 0);
    border-bottom: 5px solid rgb(131, 131, 131);
}

QScrollBar::down-arrow:vertical
{
    width: 0;
    height: 0;
    border-left: 3px solid rgba(86, 86, 86, 0);
    border-right: 3px solid rgba(86, 86, 86, 0);
    border-top: 5px solid rgb(131, 131, 131);
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}


QWidget, QLabel:enabled {
    font-family: Calibri;
    color: rgb(191, 179, 119);
    font-size: 12pt;
}
"""

APP = QApplication([])
APP.setStyleSheet(style)
DATABASE = QSqlDatabase('QSQLITE')
DATABASE.setDatabaseName(DB_FILE_PATH)





if DATABASE.open():

    window = AppMainWindow(DATABASE)
    window.show()
    sys.exit(APP.exec_())

else:
    MESSAGE.error(
        title='Ошибка базыд данных',
        text='Не удалось подключить базу данных < ' + DB_FILE_PATH + '> '
    )
















