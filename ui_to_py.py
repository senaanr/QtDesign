from PyQt5 import uic

with open('HakkindaUI.py','w',encoding="utf-8") as fout:
    uic.compileUi('Hakkinda.ui',fout)

