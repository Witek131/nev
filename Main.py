#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui',self)
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        a=2+3

        sender = self.sender()
        print(sender.text())
        self.label.setText(sender.text()+'was pressed')


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())