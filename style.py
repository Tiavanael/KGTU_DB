# -*- coding: utf-8 -*-

from paths import STYLE_PATH, os


class Style(object):
    def __init__(self):
        super(Style, self).__init__()
        self.ComboBox       =    open(os.path.join(STYLE_PATH, 'ComboBox'    )).read()
        self.Frame          =    open(os.path.join(STYLE_PATH, 'Frame'       )).read()
        self.GroupBox       =    open(os.path.join(STYLE_PATH, 'GroupBox'    )).read()
        self.Label          =    open(os.path.join(STYLE_PATH, 'Label'       )).read()
        self.LineEdit       =    open(os.path.join(STYLE_PATH, 'LineEdit'    )).read()
        self.ListWidget     =    open(os.path.join(STYLE_PATH, 'ListView'    )).read()
        self.PushButton     =    open(os.path.join(STYLE_PATH, 'PushButton'  )).read()
        self.ScrollArea     =    open(os.path.join(STYLE_PATH, 'ScrollArea'  )).read()
        self.ScrollBar      =    open(os.path.join(STYLE_PATH, 'ScrollBar'   )).read()
        self.TableWidget    =    open(os.path.join(STYLE_PATH, 'TableWidget' )).read()
        self.TabWidget      =    open(os.path.join(STYLE_PATH, 'TabWidget'   )).read()
        self.TreeWidget     =    open(os.path.join(STYLE_PATH, 'TreeWidget'  )).read()
        self.Widget         =    open(os.path.join(STYLE_PATH, 'Widget'      )).read()
        self.Message        =    open(os.path.join(STYLE_PATH, 'Message'     )).read()
        self.CheckBox       =    open(os.path.join(STYLE_PATH, 'CheckBox'    )).read()


STYLE = Style()