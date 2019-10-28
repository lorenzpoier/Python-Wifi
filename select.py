import sqlite3

conn= sqlite3.connect('students.db')
birth_year = input('geburtsjahr: ')
#sql_text = 'select * from student where birth_year=?', (birth_year,))
#print(sql_text)
cursor = conn.execute('select name, birth_year from student where birth_year = ?', (birth_year,))

for row in cursor:
	print(row)