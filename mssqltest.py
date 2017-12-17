import pymssql



conn = pymssql.connect(host='192.168.0.2', user='Администратор', password='', database='ClarisTKHP', as_dict=True)
cur = conn.cursor()

cur.execute('SELECT * FROM glo WHERE cod=%d', 1)
for row in cur:
    print(row.items)

conn.close()
