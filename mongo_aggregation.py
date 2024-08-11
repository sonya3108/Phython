# response = prod_coll.aggregate(query)
# pprint(list(response))

# match stage
query = [
    {'$match': {'contain_gluten': False}}
]
# $match stage
# query = [
#     {'$match': {'contain_gluten': False}}
# ]
# query = [
#     {'$match': {
#         # '$and': [
#         '$or': [
#             {'contain_gluten': True},
#             {'price': {'$gte': 40}},
#         ]
#         }
#     }
# ]
# response = prod_coll.aggregate(query)
# pprint(list(response))


# stage $group
# query = [
#     {
#         '$group': {'_id': '$contain_gluten'}
#     }
# ]
# response = prod_coll.aggregate(query)
# pprint(list(response))
#
# query = [
#     {
#         '$group': {'_id': {'gluten': '$contain_gluten', 'price2': '$price'}}
#     }
# ]
# response = prod_coll.aggregate(query)
# pprint(list(response))

# $sum stage


# query = [
#     {
#         '$group': {'_id': '$contain_gluten', 'count': {'$sum': '$remains'}}
#     }
# ]
# response = prod_coll.aggregate(query)
# pprint(list(response))


# final $project stage

# query = [
#     {'$project': {'_id': 0, 'contain_gluten': 1, 'title': 1, 'item_description': {'$concat': ['$title', ' - ', '$comment']}}   }
# ]
# response = prod_coll.aggregate(query)
# pprint(list(response))


# FINAL
