from PySide.QtCore import *
from PySide.QtGui import *


class Window(QDialog):

    def __init__(self):
        self.db_table = TableView(self)

    def print_table(self):
        dialog = QPrintDialog(self)
        if dialog.exec_() == dialog.Accepted:
            self.db_table.print_(dialog.printer())


class TableView(QTableView):

    def print_(self, printer):
        model = self.model()

        rows = model.rowCount()
        cols = model.columnCount()

        totalWidth = 0.0
        for i in xrange(cols):
            totalWidth += self.columnWidth(i)

        painter = QPainter(printer)

        pageSize = printer.pageRect()
        pageHeight = pageSize.height()

        scaleX = pageSize.width() / totalWidth
        painter.scale(scaleX, 1.0)

        totalHeight = 0.0

        newPage = False
        offsetY = 0
        for row in xrange(rows):

            height = self.rowHeight(row)
            totalHeight += height
            if totalHeight > pageHeight:
                totalHeight = height
                printer.newPage()
                newPage = True

            for col in xrange(cols):
                idx = model.index(row, col)
                option = self.viewOptions()
                option.rect = self.visualRect(idx)

                if newPage:
                    offsetY = option.rect.y()
                    newPage = False

                option.rect.moveTop(option.rect.y() - offsetY)
                self.itemDelegate().paint(painter, option, idx)

        painter.end()
