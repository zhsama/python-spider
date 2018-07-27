import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')

data = {
    'id': 20003,
    'name': 'Bob',
    'age': 22
}
table = 'students'
keys = ','.join(data.keys())
values = ','.join(["%s"] * len(data))

sql = 'insert into {table}({keys}) values ({values}) on duplicate key update '.format(keys=keys, values=values,
                                                                                      table=table)
update = ','.join('{key}=%s'.format(key=key) for key in data)
sql += update
cursor = db.cursor()
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        db.commit()
        print('success')
except:
    print('failed')
    db.rollback()

db.close()
