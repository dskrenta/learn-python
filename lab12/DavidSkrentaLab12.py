'''
CIS 117 Python Programing: Lab 12
David Skrenta
'''

import sqlite3

DB_NAME = 'skrenta.db'

con = sqlite3.connect(DB_NAME)
cur = con.cursor()

cur.execute('CREATE TABLE PopByRegion (region, population)')

cur.execute('INSERT INTO PopByRegion VALUES ("Central Africa", "330,993")')
cur.execute('INSERT INTO PopByRegion VALUES ("Southeastern Africa", "743,112")')
cur.execute('INSERT INTO PopByRegion VALUES ("Japan", "100,562")')

cur.execute('SELECT Region, Population FROM PopByRegion')
print(cur.fetchall())
cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
print(cur.fetchall())
cur.execute('SELECT Region FROM PopByRegion')
print(cur.fetchall())
cur.execute ('SELECT Region FROM PopbyRegion WHERE Population > 400000')
print(cur.fetchall())
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchone())
cur.execute('''UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"''')
cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
print(cur.fetchone())
cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')
cur.execute('SELECT * FROM PopByRegion')
print(cur.fetchall())

con.close()

'''
[('Central Africa', '330,993'), ('Southeastern Africa', '743,112'), ('Japan', '100,562')]
[('Central Africa', '330,993'), ('Japan', '100,562'), ('Southeastern Africa', '743,112')]
[('Central Africa',), ('Southeastern Africa',), ('Japan',)]
[('Central Africa',), ('Southeastern Africa',), ('Japan',)]
('Japan', '100,562')
('Japan', 100600)
[('Southeastern Africa', '743,112')]

'''
