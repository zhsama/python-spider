# import json
#
# with open('test.json', 'r', encoding='utf-8') as f:
#     str = f.read()
#     data = json.dumps(str)
#     print(data)
#
# print(data[0])
# print(data[0]['name'])
# print(data[0].get('name'))

import pandas
data = pandas.read_json('test.json')
print(data)