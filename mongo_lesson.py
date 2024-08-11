from uuid import uuid4

from pymongo.mongo_client import MongoClient
from bson import Decimal128

from config import USER_NAME, PASSWORD

@@ -27,9 +28,9 @@
    {'title': 'Super mop', 'price': 500, 'uuid': str(uuid4()), 'features': ['clean', 'fresh']},
    {'title': 'Super mop6', 'price': 666, 'uuid': str(uuid4())},
    {'title': 'Super mop', 'price': 555, 'uuid': str(uuid4())},
    {'title': 'Super mop', 'price': 200, 'uuid': str(uuid4())},
    {'title': 'Jabk Super mop 77  88 dec', 'price': Decimal128(str(222.14)), 'uuid': str(uuid4())},
]
mops_coll.insert_many(docs)
# mops_coll.insert_many(docs)

# READ DATA
# first
@@ -49,7 +50,7 @@
# for doc in result:
#     pprint(doc)

# query = {'price': 200}
query = {'price': 200}
# result = mops_coll.find(query)
# pprint(list(result))

@@ -64,5 +65,77 @@
             {'price': {'$gte': 200, '$lte': 400},
    'title': {'$regex': 'Su*'}}
result = mops_coll.find(query).limit(4).sort('price', -1).skip(2)
pprint(list(result))
query = {'title': {'$regex': 'JaCk*', '$options': 'i'}
}
query = {
    'title': {'$regex': 'mop 77$', '$options': 'i'}
}
query = {
    'title': {'$regex': '^Ja.k', '$options': 'i'}
}
query = {
    'title': {'$regex': '^Ja.k', '$options': 'i'}
}
query = {
    'title': {'$not': {'$regex': '^Ja.k', '$options': 'i'}}
}
# ObjectId
# query = {
#     '_id': ObjectId('66a7db5d9c16fde3914be016')
# }
# result = mops_coll.find(query).limit(4).sort('price', -1).skip(2)
# result = mops_coll.find(query).limit(4).sort('price', -1)
# result = mops_coll.find(query).sort('price', -1)
# pprint(list(result))

# print(int('66a7db5d9c16fde3914be016', 16))
          # 31770397538707243662635163670

# UPDATE

# use $set
# query = {'price': 200}
# new_data = {'$set': {'brand': 'Mr Cleaner many', 'price': 250}}
# # data = mops_coll.update_one(query, new_data)
# data = mops_coll.update_many(query, new_data)
# print(data.raw_result)

# use multiplication
# query = {}
# operation = {'$mul': {'price': Decimal128(str(1.2))}}
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)

# increase
# query = {}
# operation = {'$inc': {'price': 10, 'warranty': -4}, '$mul': {'cost': Decimal128(str(1.2))}}
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)


# DELETE fields

# query = {'price': {'$gt': 1000}}
# operation = {'$unset': {'warranty': 1}}
# data = mops_coll.update_many(query, operation)
# print(data.raw_result)

# DELETE document

# query = {'price': {'$gt': 1000}}
# data = mops_coll.delete_many(query)
# print(data.deleted_count)


# mops_coll.drop()
# client.drop_database(db)
