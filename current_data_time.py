#!/usr/bin/python3
from PyQt5.QtCore import QDate, QTime, QDateTime,  Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
