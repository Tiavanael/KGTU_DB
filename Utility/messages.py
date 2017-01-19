
#PYQT
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui  import QIcon, QFont

#WIDGET
from Widgets.ListWidget import MYListWidget
from PyQt5.QtWidgets import QVBoxLayout, QListWidgetItem
from Widgets.Dialog  import MYDialog
from Widgets.Label   import MYLabel
from Widgets.Image   import MYImage

# ICONS
from icons import ICON

#namespace
from app_namespace import APP








class LineMessage(MYDialog):
    """
    line structure = [{message_type: CGPC_MSG_TYPE}, ...]
    """
    def __init__(self, message_lines, title):
        super(LineMessage, self).__init__()

        self.__init_Attributes()
        self.__init_Parameters(title, message_lines)
        self.__init_Layouting()




    # inits
    def __init_Attributes(self):
        self.area = MYListWidget(parent=self)
        self.icon_height = 50

    def __init_Parameters(self, title, message_lines):
        self.setWindowTitle(title)
        self.close_btn.hide()
        self.setWindowModality(Qt.WindowModal)
        font = QFont()
        font.setPointSize(12)
        self.area.setFont(font)
        self.area.setIconSize(QSize(50, self.icon_height))

        for line in message_lines:
            _type = list(line.keys())[0]
            mssg = line[_type]

            item = QListWidgetItem(mssg)

            if _type == APP.MSG_SUCCESS or type == 'success':
                item.setIcon(QIcon(ICON.DIALOG.accept()))
            elif _type == APP.MSG_WARNING:
                item.setIcon(QIcon(ICON.DIALOG.warning()))
            elif _type == APP.MSG_ERROR:
                item.setIcon(QIcon(ICON.DIALOG.error()))
            elif _type == APP.MSG_INFO:
                item.setIcon(QIcon(ICON.DIALOG.info()))

            self.area.addItem(item)

        self.resize(480, int(self.icon_height*len(message_lines)) + int(self.icon_height*2))

    def __init_Layouting(self):
        self.main_layout.addWidget(self.area)


    def close(self):
        super(LineMessage, self).close()
        self.area.clear()




class DefaultMessages(MYDialog):

    #SIGNALS



    def __init__(
            self,
            name,
            message,
            mssg_type = 'info',
            btn_Cancel = True
    ):
        super(DefaultMessages, self).__init__(
            title=name,
            layout='H'
        )

        self.__init_Attributes(mssg_type)
        self.__init_Parameters(message)
        self.__init_Layouting()




    #inits
    def __init_Attributes(self, mssg_type):
        self.msg_type = mssg_type
        self.layout   = QVBoxLayout()
        self.image    = MYImage(parent=self)
        self.text     = MYLabel(parent=self)

    def __init_Parameters(self, message):
        self.setFixedSize(400, 150)

        self.text.setText(message)
        self.text.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.text.setWordWrap(True)

        self.image.setFixedSize(128, 128)

        if  self.msg_type == 'info':
            map_path = ICON.DIALOG.info()
        elif self.msg_type == 'error':
            map_path = ICON.DIALOG.error()
        elif self.msg_type == 'warning':
            map_path = ICON.DIALOG.warning()
        elif self.msg_type == 'accept':
            map_path = ICON.DIALOG.accept()

        self.image.setImagePath(map_path)

    def __init_Layouting(self):
        self.main_layout.addWidget(self.image)
        self.main_layout.addWidget(self.text)




class Message(object):
    def __init__(self):
        super(Message, self).__init__()

    def info(self, title, text):
        dialog = DefaultMessages(name=title,
                                 message=text,
                                 mssg_type='info',
                                 btn_Cancel=False)
        return dialog.exec_()

    def error(self, title, text):
        dialog = DefaultMessages(
            name=title,
            message=text,
            mssg_type='error',
            btn_Cancel=False
        )
        return dialog.exec_()

    def warning(self, title, text, ):
        dialog = DefaultMessages(
            name=title,
            message=text,
            mssg_type='warning',
            btn_Cancel=False
        )
        return dialog.exec_()

    def accept(self, title, text, ):
        dialog = DefaultMessages(name=title,
                                 message=text,
                                 mssg_type='accept',
                                 btn_Cancel=False)
        return dialog.exec_()

    def lines(self, message_list, title):
        """
        message_types = CGPC.MSG_TYPES
        :param message_list = [{message_type: message}, ...]:
        :param title = str
        :return: dialog result
        """
        dialog = LineMessage(
            message_lines=message_list,
            title=title
        )
        return dialog.exec_()





MESSAGE = Message()






if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    title = 'Test'
    msg = 'Dialog message'
    MESSAGE.accept(title, msg)