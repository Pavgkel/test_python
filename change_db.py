import psycopg2
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidget
from PyQt5.QtWidgets import QTableWidgetItem, QWidget, QPushButton, QLineEdit

def add_author():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute(f"insert into readers (name, addres, telefon) values ('Vasiliy', 'Perm', {28})")
        conn.commit()

#добавить запись
def ins(table,name1,name2,name3,name4,param1,param2,param3,param4):
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute(f"insert into {table} ({name1}, {name2}, {name3},{name4}) values ('{param1}', '{param2}', '{param3}', '{param4}')")
        conn.commit()

def ins_reader(table,name1,name2,name3,param1,param2,param3):
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute(f"insert into {table} ({name1}, {name2}, {name3}) values ('{param1}', '{param2}', '{param3}')")
        conn.commit()

def ins_lending_books(table,name1,name2,name3,name4,name5,param1,param2,param3,param4,param5):
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute(f"insert into {table} ({name1}, {name2}, {name3}, {name4}, {name5}) values ('{param1}', '{param2}', '{param3}','{param4}','{param5}')")
        conn.commit()

def change_lending_books(table,element1,element2, name1, name2, name3, name4, name5, param1, param2, param3, param4, param5):
    with psycopg2.connect(user="postgres",
                            password="1",
                            host="localhost",
                            port="5432",
                            database="library2") as conn:
        cur = conn.cursor()
        ids = int(element1)  # идентификатор строки
        ids2=int(element2)
        cur.execute(f"Update  {table} set {name1}='{param1}',{name2}='{param2}',{name3}='{param3}',{name4}='{param4}',{name5}='{param5}' where id_book = {ids} and id_reader={ids2}")
        conn.commit()
# удалить из таблицы строку
def dels(element,table):
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        ids = int(element) # идентификатор строки
        cur.execute(f"delete from {table} where id={ids}")
        conn.commit()

# обновить запись
def change(table,element,name1,name2,name3,name4,param1,param2,param3,param4):

    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        ids = int(element)  # идентификатор строки
        cur.execute(f"Update {table} set {name1}='{param1}',{name2}='{param2}',{name3}='{param3}',{name4}='{param4}' where id = {ids}")
        conn.commit()

def change_reader(table,element,name1,name2,name3,param1,param2,param3):

    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        ids = int(element)  # идентификатор строки
        cur.execute(f"Update {table} set {name1}='{param1}',{name2}='{param2}',{name3}='{param3}' where id = {ids}")
        conn.commit()
#количество книг в библиотеке
def count_book():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) from books where in_library=true")

    return cur.fetchall()
# количество читателей
def count_readers():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) from readers")
    return cur.fetchall()
#количество книг, который брал каждый читатель за все время
def count_books():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute("SELECT readers.name,Count(*) from lending_books inner join readers on lending_books.id_reader=readers.id Group by readers.name")
    return cur.fetchall()
#количество книг у читателя
def count_reader_book():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute("Select readers.name, COUNT(*) from lending_books inner join readers on lending_books.id_reader=readers.id where data_return Is Null Group by readers.name")
    return cur.fetchall()
#дата последнего посещения читетелем библиотеки
def reader_last(element):
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        ids = int(element)  # идентификатор строки
        cur.execute(f"Select MAX(data_issue) from lending_books where id_reader={ids}")
    return cur.fetchall()
#самый читаемый автор
def max_author():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute(f"select author from books where id in (Select count(author) from books left join lending_books on books.id = lending_books.id_book group by author)")
        return cur.fetchall()
#самые предпочитаемые жанры
def genre():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute(f"select genre from books left join lending_books on books.id = lending_books.id_book order by genre desc")
    return cur.fetchall()
#любимый жанр каждого читателя
def love_genre():
    with psycopg2.connect(user="postgres",
                          password="1",
                          host="localhost",
                          port="5432",
                          database="library2") as conn:
        cur = conn.cursor()
        cur.execute(f"select readers.name,max(genre) from readers inner join lending_books on readers.id=lending_books.id_reader inner join books on books.id=lending_books.id_book group by readers.name")
    return cur.fetchall()