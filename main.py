'''
ЗАДАНИЕ
- Напишите функцию, которая считает количество гласных в строке, и создайте тесты для этой функции.
- Проверьте, что функция правильно считает гласные в строке, содержащей только гласные.
- Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
- Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).
'''
import sqlite3


def check(number):
   return number % 2 == 0


def is_palindrome(s):
   return s == s[::-1]


def sort_list(numbers):
   return sorted(numbers)


def init_db():
   conn = sqlite3.connect(':memory:')
   cursor = conn.cursor()
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   name TEXT,
   age INTEGER)
   ''')
   return conn

def add_user(conn, name, age):
   cursor = conn.cursor()
   cursor.execute('''
   INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
   conn.commit()

def get_user(conn, name):
   cursor = conn.cursor()
   cursor.execute('''SELECT * FROM users WHERE name=?''', (name,))
   return cursor.fetchone()
