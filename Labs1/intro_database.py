from pymongo import MongoClient

uri = "mongodb://admin2:admin123@ds137631.mlab.com:37631/rosenguyen_c4e19_lab"

#1. Connect to database
client = MongoClient(uri)

#2. Get database
db = client.get_default_database()

#3. Create collection
mau_quan_ao = db['mau_quan_ao']

# #4. Create document
# mau_ao = {
#     "ten": "ao dinh saquein",
#     "price": "US1500$",
# }
# #5. Insert document into collection
# mau_quan_ao.insert_one(mau_ao)

# 6.Get all documents

all_games = mau_quan_ao.find()

print(all_games[0]['ten'])