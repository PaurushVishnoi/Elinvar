import re, sqlite3
import parameters

#Connection to the database
conn = sqlite3.connect('elinvarDatabase.db')
c = conn.cursor()
id = '9700'
def_val = c.execute('SELECT (julianday("2015-10-28T12:24:34.002")-julianday("2015-10-28T12:24:33.903"))*8640')

print(def_val.fetchall()[0][0])