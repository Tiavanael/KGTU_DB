# -*- coding: utf-8 -*-


#Unicode
import unicodedata as unicode

#Qt Classes
from PyQt5.QtGui import QFont


#WIDGETS
from PyQt5.QtWidgets import QTextEdit


#PARAMETERS
from parameters import FONT_SIZE



class MYTextEdit(QTextEdit):
    
    #INIT
    def __init__(self, parent=None):
        super(MYTextEdit, self).__init__()
        
        
        # ATTRIBUTES-------------------------------------
        # END ATTRIBUTES---------------------------------
        

        # PARMS------------------------------------------
        if parent: self.setParent(parent)

        font = QFont()
        font.setPointSize(FONT_SIZE)

        self.setFont(font)
        
        # END PARMS--------------------------------------



    
    #EVENTS-----------------------------------------------
    #END EVENTS-------------------------------------------
    
    
    
    # METHODES--------------------------------------------
    # END METHODES----------------------------------------
        
        
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWidgets import QPushButton
    app = QApplication([])
    p = QPushButton()
    win = MYTextEdit()
    win.show()
    p.show()
    app.exec_()