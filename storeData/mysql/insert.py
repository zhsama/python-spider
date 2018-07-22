import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
# id = 20001
# user = 'Bob'
# age = 20
# cursor = db.cursor()
# sql = 'insert into students(id,user,age) values (%s,%s.%s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
#
# db.close()

# 标准写法
data = {
    'id': 20003,
    'name': 'Jordan1',
    'age': 22
}
table = 'students'
keys = ','.join(data.keys())  # 写入data的key
values = ','.join(['%s'] * len(data))  # 为values提供占位符%s
sql = "insert into {table}({keys}) values({values})".format(keys=keys, values=values, table=table)
cursor = db.cursor()
try:
    if cursor.execute(sql, tuple(data.values())):
        db.commit()
        print('insert success')
except:
    print('insert failed')
    db.rollback()

db.close()
