# coding:utf-8
# openfiledialog.py
from PySide.QtCore import *
from PySide.QtGui import (QMainWindow, QWidget, QTextEdit, QAction, QIcon,
                          QFileDialog, QApplication)
import sys


class OpenFile(QMainWindow):

    def __init__(self, parent=None):
        super(OpenFile, self).__init__()
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('OpenFile')
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()
        exit = QAction(QIcon('icons.png'), 'Open', self)
        exit.setShortcut('Ctrl+O')
        exit.setStatusTip('Open new file')
        # self.connect(exit, QtCore.SIGNAL('triggered()'), self.showDialog)
        exit.triggered.connect(self.showDialog)
        mb = self.menuBar()
        file = mb.addMenu('&File')
        file.addAction(exit)

    def showDialog(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', '')
        file = open(filename)

        data = file.read()
        self.textEdit.setText(data)


app = QApplication(sys.argv)
cd = OpenFile()
cd.show()
sys.exit(app.exec_())
