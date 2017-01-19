from PyQt5.QtCore import QDate
from PyQt5.QtCore import QDateTime




dt = QDate(2007, 10, 10)
d = QDateTime()
d.setDate(dt)
print(d)
print(d.toPyDateTime())