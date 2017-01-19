


import os, sys
from parameters import OS




def getRoot(*arg):
    app_path = ''
    if getattr(sys, 'frozen', False):
        dir_name = os.path.dirname(sys.executable)
        app_path = os.path.abspath(dir_name)
    else:
        app_path = os.path.dirname(__file__)

    if arg:
        app_path = os.path.join(app_path, os.path.join(*arg))

    return app_path




ROOT = getRoot()




if   OS == 'posix': DEFAULT_DIALOG_PATH = '/home/'
elif OS == 'nt':    DEFAULT_DIALOG_PATH = 'C:/'




RESOURCES_PATH = os.path.join(ROOT, 'Resources')
STYLE_PATH     = os.path.join(RESOURCES_PATH, 'StyleFiles')
ICONS_PATH     = os.path.join(RESOURCES_PATH, 'Icons')
DB_PATH        = os.path.join(ROOT, 'DataBase')
DB_FILE_PATH   = os.path.join(DB_PATH, 'app_data_base.db')

