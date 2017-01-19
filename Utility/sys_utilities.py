
import json
import os

#ERRORS
from Utility.errors import ERROR





class SysUtil(object):
    def __init__(self):
        super(SysUtil, self).__init__()

    #PATHS AND FILES
    def makeDirs(self, path):
        if not os.path.exists(path):
            os.makedirs(path)


    def saveToJSON(self, obj, path):
        if not os.path.exists(path):
            new_file = open(path, 'w')
            new_file.close()
            if os.path.exists(path):
                json.dump(
                    obj=obj,
                    fp=open(path, 'w'),
                    indent=4
                )
        else:
            json.dump(
                obj=obj,
                fp=open(path, 'w'),
                indent=4
            )


    def loadFromJSON(self, path):
        if (os.path.exists(path)):
            result = json.load(fp=open(path))
            return result
        else:
            ERROR.fileNotExist(
                cls='SysUtil',
                mthd='loadFromJSON()',
                path=path
            )


    def goodFileName(self, name):
        """
        Возвращает True, если имя не имеет
        непригодных символов в для имён файлов ОС

        :param name: путь (str)
        :return: bool
        """
        good = True
        for sign in name:
            badSign = r':*?"<>|/\\'
            if (badSign.find(sign) != -1):
                good = False
                break
        if good:
            return True
        else:
            return False


    def fileWithoutExt(self, name=''):
        return name.split('.')[0]


    def getFileExt(self, file_path=''):
        ext = ''
        try:
            ext = file_path.split('.')[-1]
        except:
            ext = ''
        return ext


    def basePath(self, paths=[]):
        """
        Возвращает базовый путь для заданных путей.
        Пример:
        :param paths = [
                    'C:/Home/Image',
                    'C:/Home/Video',
                    'C:/Home/Porn',
                ]
        :return: 'C:/Home/
        """
        return os.path.commonprefix(paths)


    #DICTS
    def renameKey(self, old_kye, new_key, dct):
        if old_kye in dct:
            if new_key != old_kye:
                val = dct[old_kye]
                dct.pop(old_kye)
                dct[new_key] = val


    def keyFromValue(self, val, dct={}):
        """
        Возвращает ключ, который соответствует значению <val>
        Если значение <val> не одно, возвращает первый ключ,
        которому соответсвует значение <val>

        :param val:
        :param dct:
        :return: key
        """
        result = None
        for key in dct:
            if dct[key] == val:
                result = key
                break
        return result


    def existInContainer(self, except_name, name, container):
        """
        Проверяет, есть ли <name> в
        контейнере <container>,
        но пропускает <except_name>

        :param except_name: элемент-исключение
        :param name: проаеряемый элемент
        :param container: контейнер для проверки
        :return: bool
        """
        result = False
        for itm in container:
            if itm != except_name:
                if itm == name:
                    result = True
                    break
        return result





SYSUTIL = SysUtil()