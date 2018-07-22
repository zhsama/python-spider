import pymysql

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='spiders')
table = 'students'
condition = 'age>21'
sql = "delete from {table} where {condition}".format(table=table, condition=condition)
cursor = db.cursor()
try:
    if cursor.execute(sql):
        print("delete success")
        db.commit()
except:
    print("delete failed")
    db.rollback()

db.close()
