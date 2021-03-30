import pyodbc

conn = pyodbc.connect('DSN=[DATA SOURCE NAME];UID=[USER];PWD=[PASSWORD]')

# Encoding and decoding specific to NonStop SQL/MX
conn.setdecoding(pyodbc.SQL_CHAR, encoding='iso-8859-1')
conn.setdecoding(pyodbc.SQL_WCHAR, encoding='iso-8859-1')
conn.setencoding(encoding='iso-8859-1')

cursor = conn.cursor()
cursor.execute('INSERT INTO CATALOG.SCHEMA.TABLE VALUES (VALUE1, VALUE2)')

# makes sure that insert statement is a committed transaction in NonStop SQL/MX database
conn.commit()

# prints table to make sure that data was updated
cursor.execute('SELECT * FROM CATALOG.SCHEMA.TABLE')
for row in cursor:
    print(row)
