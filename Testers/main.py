import sys

from PyQt5.QtWidgets import QApplication


class PQApplication(QApplication):

    def __init__(self, args):
        super(QApplication, self).__init__(args)

        try:
            file = open("locked")
            text = file.readline()
            file.close()
        except:
            text = ""
        if not (text == "true"):
            file = open("locked", "w")
            file.write("true")
            file.close()
            print("Приложение запущено!")
        else:
            print("Приложение уже было запущено!")
            sys.exit()

    def exec_(self):
        super(QApplication, self).exec()
        open("locked", "w").close()
        print("Приложение закрыто!")

if __name__ == "__main__":
    import Testers.appClasses

    app = Testers.appClasses.Application()
    app.start()

