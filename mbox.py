import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit, QMessageBox, QTableWidget, QSizePolicy, \
    QApplication


class MyMessageBox(QMessageBox):
    def __init__(self,result1):
        self.result1=result1
        QMessageBox.__init__(self)

        self.setSizeGripEnabled (True)

        self.setWindowTitle ('Hello MessageBox')


        #Add TableWidget to QMessageBox
        self.addTableWidget (self)
        currentClick = self.exec_()


        #Create TableWidget
    def addTableWidget (self, parentItem) :
        self.tableWidget = QTableWidget(parentItem)
        self.tableWidget.setGeometry (QRect(0, 0, 540, 250))
        self.tableWidget.setObjectName ('tableWidget')

        self.tableWidget.setColumnCount(2)


        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(['Результат'])  # заголовки столцов

        rows = self.result1
        i = 0
        for elem in rows:
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            j = 0
            for t in elem:  # заполняем внутри строки
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1

        self.tableWidget.resizeColumnsToContents()
    #Allow resizing of QMessageBox
    def event(self, e):
        result = QMessageBox.event(self, e)
        self.setMinimumWidth(0)
        self.setMaximumWidth(16777215)
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.resize(550, 300)

        return result

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyMessageBox ()
    #ex.show()
    sys.exit(app.exec_())