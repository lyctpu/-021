import sqlite3


connection = sqlite3.connect('Matthew.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Matthew
              (Title TEXT, Director TEXT, Year INT)''')


connection.commit()
connection.close()
