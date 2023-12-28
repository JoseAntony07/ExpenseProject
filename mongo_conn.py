import pymongo


client = pymongo.MongoClient("localhost", 27017)

db = client.expense

expense_collection = db.expense

print(expense_collection)
