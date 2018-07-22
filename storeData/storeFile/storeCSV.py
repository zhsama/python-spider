import csv
import pandas

# with open('test.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 23])

# with open('test.csv', 'w', encoding='utf-8') as f:
#     writer = csv.writer(f, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 23])

# with open('test.csv','r',encoding='utf-8') as f:
#     data = csv.reader(f)
#     for i in data:
#         print(i)

# with open('test.csv', 'a', encoding='utf-8') as f:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({"id": "10001", "name": "Mike", "age": 20})
#     writer.writerow({"id": "10002", "name": "Bob", "age": 22})
#     writer.writerow({"id": "10003", "name": "Jordan", "age": 23})

# with open('test.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in  reader:
#         print(row)

# file = pandas.read_csv('test.csv')
# print(file)