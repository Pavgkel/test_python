from datetime import datetime

from PyQt5 import QtWidgets
import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit, QMessageBox
import sys
from MainForm import Ui_MainWindow
import change_db as ll
import mbox as mb
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Библиотека')
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget_2.setColumnCount(4)
        self.ui.tableWidget_3.setColumnCount(5)
        self.ui.tableWidget.verticalHeader().hide()
        self.ui.tableWidget_2.verticalHeader().hide()
        self.ui.tableWidget_3.verticalHeader().hide()
        self.updt_book()
        self.updt_reader()
        self.updt_lending_book()
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)  # запретить изменять поля
        self.ui.tableWidget.cellClicked.connect(self.cellClick_book)
        self.ui.tableWidget_2.cellClicked.connect(self.cellClick_reader)
        self.ui.tableWidget_3.cellClicked.connect(self.cellClick_lending_book)
        self.ui.pushButton.clicked.connect(self.add_books)
        self.ui.pushButton_2.clicked.connect(self.del_book)
        self.ui.pushButton_3.clicked.connect(self.change_book)
        self.ui.pushButton_8.clicked.connect(self.add_reader)
        self.ui.pushButton_7.clicked.connect(self.del_reader)
        self.ui.pushButton_9.clicked.connect(self.change_reader)
        self.ui.pushButton_10.clicked.connect(self.add_lending_book)
        self.ui.pushButton_11.clicked.connect(self.change_lending_book)

        self.ui.action.triggered.connect(self.clickMethod1)
        self.ui.action_2.triggered.connect(self.clickMethod2)
        self.ui.action_3.triggered.connect(self.clickMethod3)
        self.ui.action_4.triggered.connect(self.clickMethod4)
        self.ui.action_5.triggered.connect(self.clickMethod5)
        self.ui.action_6.triggered.connect(self.clickMethod6)
        self.ui.action_7.triggered.connect(self.clickMethod7)
        self.ui.action_8.triggered.connect(self.clickMethod8)

    #заполнитель для книги
    def updt_book(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setHorizontalHeaderLabels(['id', 'Книга', 'Автор', 'В библиотеке','Жанр'])  # заголовки столцов
        with psycopg2.connect(user="postgres",
                              password="1",
                              host="localhost",
                              port="5432",
                              database="library2") as conn:
            self.cur = conn.cursor()
            self.cur.execute("select * from books")
        rows = self.cur.fetchall()
        i = 0
        for elem in rows:
            self.ui.tableWidget.setRowCount(self.ui.tableWidget.rowCount() + 1)
            j = 0
            for t in elem:  # заполняем внутри строки
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1

        self.ui.tableWidget.resizeColumnsToContents()
    #заполнитель для читателя
    def updt_reader(self):
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(['id', 'Читатель', 'Адрес', 'Телефон'])  # заголовки столцов
        with psycopg2.connect(user="postgres",
                              password="1",
                              host="localhost",
                              port="5432",
                              database="library2") as conn:
            self.cur = conn.cursor()
            self.cur.execute("select * from readers")
        rows = self.cur.fetchall()
        i = 0
        for elem in rows:
            self.ui.tableWidget_2.setRowCount(self.ui.tableWidget_2.rowCount() + 1)
            j = 0
            for t in elem:  # заполняем внутри строки
                self.ui.tableWidget_2.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1

        self.ui.tableWidget_2.resizeColumnsToContents()
    #заполнитель для выданных книг
    def updt_lending_book(self):
        self.ui.tableWidget_3.clear()
        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_3.setHorizontalHeaderLabels(['id книги','id читателя','Дата приема', 'Дата планируемого возврата','Дата возврата'])  # заголовки столцов
        with psycopg2.connect(user="postgres",
                              password="1",
                              host="localhost",
                              port="5432",
                              database="library2") as conn:
            self.cur = conn.cursor()
            self.cur.execute("select * from lending_books")
        rows = self.cur.fetchall()
        i = 0
        for elem in rows:
            self.ui.tableWidget_3.setRowCount(self.ui.tableWidget_3.rowCount() + 1)
            j = 0
            for t in elem:  # заполняем внутри строки
                self.ui.tableWidget_3.setItem(i, j, QTableWidgetItem(str(t).strip()))
                j += 1
            i += 1

        self.ui.tableWidget_3.resizeColumnsToContents()

    #обработчик для книги
    def cellClick_book(self, row, col): # row - номер строки, col - номер столбца
        self.id=self.ui.tableWidget.item(row, 0).text().strip()
        self.ui.lineEdit.setText(self.ui.tableWidget.item(row, 1).text().strip())
        self.ui.lineEdit_2.setText(self.ui.tableWidget.item(row, 2).text().strip())
        self.ui.checkBox.setChecked(eval(self.ui.tableWidget.item(row, 3).text()))
        self.ui.lineEdit_4.setText(self.ui.tableWidget.item(row, 4).text().strip())

    #обработчик для читателя
    def cellClick_reader(self, row, col): # row - номер строки, col - номер столбца
        self.id2=self.ui.tableWidget_2.item(row, 0).text().strip()
        self.ui.lineEdit_3.setText(self.ui.tableWidget_2.item(row, 1).text().strip())
        self.ui.lineEdit_7.setText(self.ui.tableWidget_2.item(row, 2).text().strip())
        self.ui.lineEdit_8.setText(self.ui.tableWidget_2.item(row, 3).text().strip())

    # обработчик для читателя
    def cellClick_lending_book(self, row, col):  # row - номер строки, col - номер столбца
        self.id3 = self.ui.tableWidget_3.item(row, 0).text().strip()
        self.id4 = self.ui.tableWidget_3.item(row, 1).text().strip()
        self.ui.lineEdit_5.setText(self.ui.tableWidget_3.item(row, 0).text().strip())
        self.ui.lineEdit_10.setText(self.ui.tableWidget_3.item(row, 1).text().strip())
        #print(datetime.strptime(self.ui.tableWidget_3.item(row,2).text(),"%Y-%m-%d").date())
        self.ui.dateEdit.setDate(datetime.strptime(self.ui.tableWidget_3.item(row,2).text(),"%Y-%m-%d").date())
        self.ui.dateEdit_2.setDate(datetime.strptime(self.ui.tableWidget_3.item(row,3).text(),"%Y-%m-%d").date())
        self.ui.dateEdit_3.setDate(datetime.strptime(self.ui.tableWidget_3.item(row,4).text(),"%Y-%m-%d").date())

    #обновление полей книги
    def upd_book(self):
        self.updt_book()
        self.ui.lineEdit.setText('')
        self.ui.lineEdit_2.setText('')
        self.ui.lineEdit_4.setText('')
        self.ui.checkBox.setChecked(False)
    #обновление полей читателя
    def upd_reader(self):
        self.updt_reader()
        self.ui.lineEdit_3.setText('')
        self.ui.lineEdit_7.setText('')
        self.ui.lineEdit_8.setText('')

    # обновление полей выданных книг
    def upd_lending_book(self):
        self.updt_lending_book()
        self.ui.lineEdit_5.setText('')
        self.ui.lineEdit_10.setText('')
        self.ui.dateEdit.clear()
        self.ui.dateEdit_2.clear()
        self.ui.dateEdit_3.clear()

    #добавление книги
    def add_books(self):
        #print(self.ui.checkBox.isChecked())
        name1, author1, in_library1,genre1 = self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.checkBox.isChecked(),self.ui.lineEdit_4.text()

        ll.ins('books','name','author','in_library','genre',name1,author1,in_library1,genre1)
        self.upd_book()
    #удаление книги
    def del_book(self):
        ll.dels(self.id,'books')
        self.upd_book()
    #изменение книги
    def change_book(self):
        name1, author1, in_library1,genre1 = self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.checkBox.isChecked(),self.ui.lineEdit_4.text()
        ll.change('books',self.id,'name','author','in_library','genre',name1,author1,in_library1,genre1)
        self.upd_book()
    #добавление читателя
    def add_reader(self):
        name1, addres1, telefon1 = self.ui.lineEdit_3.text(), self.ui.lineEdit_7.text(), self.ui.lineEdit_8.text()
        ll.ins_reader('readers', 'name', 'addres', 'telefon',  name1, addres1, telefon1)
        self.upd_reader()
    #удаление читателя
    def del_reader(self):
        ll.dels(self.id2,'readers')
        self.upd_reader()
    #обновление читателя
    def change_reader(self):
        name1, addres1, telefon1 = self.ui.lineEdit_3.text(), self.ui.lineEdit_7.text(), self.ui.lineEdit_8.text()
        ll.change_reader('readers', self.id2, 'name', 'addres', 'telefon', name1, addres1, telefon1)
        self.upd_reader()

    # изменение выданной книги
    def change_lending_book(self):
        id1, id2, data1, data2, data3 = self.ui.lineEdit_5.text(), self.ui.lineEdit_10.text(), self.ui.dateEdit, self.ui.dateEdit_2, self.ui.dateEdit_3
        data1 = datetime.strptime(data1.text().strip(), "%Y-%m-%d")
        data2 = datetime.strptime(data2.text().strip(), "%Y-%m-%d")
        data3 = datetime.strptime(data3.text().strip(), "%Y-%m-%d")
        ll.change_lending_books('lending_books',self.id3,self.id4, 'id_book', 'id_reader', 'data_issue','data_plan','data_return', id1, id2, data1,data2,data3)
        self.upd_lending_book()

    # добавление выданной книги
    def add_lending_book(self):
        id1, id2, data1,data2,data3 = self.ui.lineEdit_5.text(), self.ui.lineEdit_10.text(), self.ui.dateEdit,self.ui.dateEdit_2,self.ui.dateEdit_3
        #print(data1.text())
        data1=datetime.strptime(data1.text().strip(),"%Y-%m-%d")
        data2 = datetime.strptime(data2.text().strip(), "%Y-%m-%d")
        data3 = datetime.strptime(data3.text().strip(), "%Y-%m-%d")
        ll.ins_lending_books('lending_books', 'id_book', 'id_reader', 'data_issue','data_plan','data_return', id1, id2, data1,data2,data3)
        self.upd_lending_book()

    def clickMethod1(self):
        info=ll.count_book()
        mb.MyMessageBox(result1=info)

    def clickMethod2(self):
        info=ll.count_readers()
        mb.MyMessageBox(result1=info)

    def clickMethod3(self):
        info=ll.count_books()
        mb.MyMessageBox(result1=info)

    def clickMethod4(self):
        info=ll.count_reader_book()
        mb.MyMessageBox(result1=info)

    def clickMethod5(self):
        info=ll.reader_last(self.id2)
        mb.MyMessageBox(result1=info)

    def clickMethod6(self):
        info=ll.max_author()
        mb.MyMessageBox(result1=info)

    def clickMethod7(self):
        info=ll.genre()
        mb.MyMessageBox(result1=info)

    def clickMethod8(self):
        info=ll.love_genre()
        mb.MyMessageBox(result1=info)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())