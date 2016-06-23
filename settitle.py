# coding: utf-8
import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(150, 150, 500, 300)
        self.setWindowTitle("PyQT tuts")
        #self.setWindowIcon(QtGui.QIcon(""))
        extractAction = QtGui.QAction("&GET TO THE COh!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leav the app")
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(100, 100)
        btn.move(100, 100)

    def close_application(self):
        print("whooaa")
        self.setWindowTitle("PytQt Title")


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    GUI
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
