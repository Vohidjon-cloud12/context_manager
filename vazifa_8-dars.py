import time
import psycopg2
from functools import reduce
import operator
# 
# 1-masala
#
# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.end_time = time.time()
#         self.elapsed_time = self.end_time - self.start_time
#         print(f"Elapsed time: {self.elapsed_time} seconds")
#
# # Body qismida 100000 gacha sonlar ko'paytmasini hisoblash
# with Timer() as timer:
#     result = reduce(operator.mul, range(1, 100001), 1)
#     print("Calculation done ☺")
#



# class Database:
#     def __init__(self, db_name='n47', user='postgres', password='123', host='localhost', port='5432'):
#         self.db_name = db_name
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#
#     def __enter__(self):
#         self.conn = psycopg2.connect(
#             dbname=self.db_name,
#             user=self.user,
#             password=self.password,
#             host=self.host,
#             port=self.port
#         )
#         self.cursor = self.conn.cursor()
#         # Oldingi malumotlarni ko'rsatish
#         self.cursor.execute("SELECT * FROM test")
#         print("Before changes:")
#         for row in self.cursor.fetchall():
#             print(row)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             self.conn.commit()
#         else:
#             self.conn.rollback()
#         # Yangi malumotlarni ko'rsatish
#         self.cursor.execute("SELECT * FROM test")
#         print("After changes:")
#         for row in self.cursor.fetchall():
#             print(row)
#         self.cursor.close()
#         self.conn.close()
#
# # Ma'lumotlar bazasini tayyorlash
# def setup_database():
#     conn = psycopg2.connect(
#         dbname='n47',
#         user='postgres',
#         password='123',
#         host='localhost',
#         port='5432'
#     )
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS test (
#             id SERIAL PRIMARY KEY,
#             name TEXT
#         )
#     ''')
#     cursor.execute('''INSERT INTO test (name) VALUES ('Initial')''')
#     conn.commit()
#     cursor.close()
#     conn.close()
#
# setup_database()
#
# # Body qismida tablega o'zgartirish kiritish
# try:
#     with Database('n47') as db:
#         db.cursor.execute("INSERT INTO test (name) VALUES ('Modified')")
#         print("Modification done.")
# except Exception as e:
#     print("An Error Occured:", e)
#     db.conn.rollback()
# finally:
#     db.conn.close()
