import pymongo
from bson.objectid import ObjectId

# 连接数据库
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:6666')
db = client.test
collection = db.students

# 插入数据
# insert
# student1 = {
#     'id': 20180725,
#     'name': 'Bob99',
#     'age': 11,
#     'gender': 'male'
# }
# student2 = {
#     'id': 20180721,
#     'name': 'Jim',
#     'age': 21,
#     'gender': 'male'
# }
# result = collection.insert(student1, student2)
# print(result)
# insert_one&insert_all
# result = collection.insert_one(student1)
# result = collection.insert_all(student1,student2)
# print(result.inserted_id)

# 查询数据
# result1 = collection.find_one({'name': 'Bob'})
# result2 = collection.find({'age': 22})
# print(result1)
# print(result2)
# 根据_id查询
# result = collection.find_one({'_id': ObjectId('5b51c153db13d43a7416d319')})
# print(result)
# 比较符号
# results = collection.find({'age': {'$gt': 20}})
# for result in results:
#     print(result)

# 计数
# print(collection.find().count())
# print(collection.find({'gender': 'male'}).count())

# 排序
# results = collection.find().sort('name', pymongo.ASCENDING)
# print([result['name'] for result in results])

# 偏移
# results1 = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# results2 = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
# print([result['name'] for result in results1])
# print([result['name'] for result in results2])

# 更新
# update
# condition = {'name': 'Bob2'}
# student = collection.find_one(condition)
# student['age'] = 25
# result = collection.update(condition, student)
# print(result)
# $set
# result = collection.update(condition, {'$set': student})
# print(result)
# update_one&update_many
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.modified_count,result.matched_count)

# 删除
# remove
# result = collection.remove({'name':'Bob'})
# print(result)
# delete_one&delete_many
# result = collection.delete_one({'age': {'$lt': 20}})
# print(result.deleted_count)
# result = collection.delete_many({'age': {'$lt': 20}})
# print(result.deleted_count)
