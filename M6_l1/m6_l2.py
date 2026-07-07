# # SQL - structured query language
# #БД - База данных (DataBase)
# #БД SQL - Реалиционная БД
# #БД NoSql
#
import sqlite3
#
# connection = sqlite3.connect("Database.db")
#
# cursor = connection.cursor() # Доступ на управление БД
#
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER
#     )
# ''') #
#
# cursor.execute(
#     "INSERT INTO users (name, age) VALUES (?, ?)",
#     ("Adam", 25)
# )
#
# connection.commit()
#
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# connection.close()


def create_table():
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()

    cursor.execute("""
    CREATE TABLE users
    (
    id INTEGER, 
    firstname TEXT,
    lastname TEXT
    )
    """)

    connect.commit()
    connect.close()

create_table()