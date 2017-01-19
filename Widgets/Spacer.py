# coding = utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf-8:




from PyQt5.QtWidgets import QSpacerItem, QSizePolicy




class MYSpacer(QSpacerItem):
    def __init__(self, type='V'):
        if type == 'V' or type == 'v':
            super(MYSpacer, self).__init__(1, 1,
                                           QSizePolicy.Minimum,
                                           QSizePolicy.Expanding)
        elif type == 'H' or type == 'h':
            super(MYSpacer, self).__init__(1, 1,
                                           QSizePolicy.Expanding,
                                           QSizePolicy.Minimum)

