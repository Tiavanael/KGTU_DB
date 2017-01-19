# -*- coding: utf-8 -*-

from parameters   import SHOW_DEBUG_INFO



class Errors(object):

    def __init__(self, clas=None):
        super(Errors, self).__init__()

        #ATTRIBUTES
        self.clas = clas

    def error(
            self,
            mthd,
            msg,
            cls=None,
            screen_output=SHOW_DEBUG_INFO
    ):
        if cls: class_name = cls
        else: class_name = self.clas

        if screen_output:
            print('')
            print('  Class: <'+class_name+'>')
            print(' Method: <'+mthd+'>')
            print('  Error: <'+msg+'.>')
            print('')
        return {
            'Class:': class_name,
            'Method:': mthd,
            'Error:': msg
        }



    def fileNotExist(
            self,
            mthd,
            path,
            cls=None,
            screen_output=SHOW_DEBUG_INFO
    ):
        if cls: class_name = cls
        else: class_name = self.clas

        if screen_output:
            print('')
            print('  Class: <'+class_name+'>')
            print(' Method: <'+mthd+'>')
            print('  Error: <File ['+path+'] is not exist>')
            print('')
        return {
            'Class': class_name,
            'Method': mthd,
            'Error': 'File ['+path+'] is not exist'
        }



    def fileIsNull(
            self,
            mthd,
            path,
            cls=None,
            screen_output=SHOW_DEBUG_INFO
    ):
        if cls: class_name = cls
        else: class_name = self.clas

        if screen_output:
            print('')
            print('  Class: <'+class_name+'>')
            print(' Method: <'+mthd+'>')
            print('  Error: <File ['+path+'] is null>')
            print('')
        return {
            'Class': class_name,
            'Method': mthd,
            'Error': 'File ['+path+'] is null'
        }



    def pathNotExist(
            self,
            mthd,
            path,
            cls=None,
            screen_output=SHOW_DEBUG_INFO
    ):

        if cls: class_name = cls
        else: class_name = self.clas

        if screen_output:
            print('')
            print('  Class: <'+class_name+'>')
            print(' Method: <'+mthd+'>')
            print('  Error: <Path ['+path+'] is not exist>')
            print('')
        return {
            'Class': class_name,
            'Method': mthd,
            'Error': 'Path ['+path+'] is not exist'
        }



ERROR = Errors()