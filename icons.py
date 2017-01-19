# -*- coding: utf-8 -*-

import os

from paths import ICONS_PATH

ICONS_PATH_DIALOG     = os.path.join(ICONS_PATH, 'Dialogs')
ICONS_PATH_APP        = os.path.join(ICONS_PATH, 'App')
ICONS_PATH_DEFAULT    = os.path.join(ICONS_PATH, 'Defaults')



class Dialogs(object):
    def __init__(self):
        super(Dialogs, self).__init__()
        pass

    def error(self):
        return os.path.join(ICONS_PATH_DIALOG, 'error.png')

    def warning(self):
        return os.path.join(ICONS_PATH_DIALOG, 'warning.png')

    def info(self):
        return os.path.join(ICONS_PATH_DIALOG, 'info.png')

    def accept(self):
        return os.path.join(ICONS_PATH_DIALOG, 'accept.png')



class Default(object):
    def __init__(self):
        super(Default, self).__init__()
        pass

    def badImageFormat(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'bad_format.png')

    def add(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'add.png')

    def remove(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'remove.png')

    def OK(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'OK.png')

    def cancel(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'cancel.png')

    def clear(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'clear.png')

    def edit(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'edit.png')

    def file(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'file.png')

    def folder_open(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'open_folder.png')

    def folder_close(self):
        return os.path.join(ICONS_PATH_DEFAULT, 'close_folder.png')



class Icons(object):
    def __init__(self):
        super(Icons, self).__init__()

        self.DIALOG      = Dialogs()
        self.DEFAULT     = Default()





ICON = Icons()