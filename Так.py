import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Slslovo.ui', self)
        self.pushButton.clicked.connect(self.sl)
        self.pushButton.clicked.connect(self.loadText)

    def loadText(self):
        with open('input.txt', encoding="utf8") as f:
            self.textBrowser.setText(f.read())

    def sl(self):
        data = open("input.txt", encoding="utf8").read()
        data.split()
        print(data)
        k = 0
        m = 100000
        f = 0
        for i in range(len(data)):
            if int(data[i]) > k:
                k = data[i]
            elif int(data[i]) < m:
                m = data[i]
            f += int(data[i])
        it = f / len(data)
        print(k)
        g = str(k) + ' ' + str(m) + ' ' + str(it)
        self.textBrowser_2.setText(g)








app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
