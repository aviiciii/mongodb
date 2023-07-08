
from pymongo import MongoClient

MONGO_DB_URI = 'mongodb+srv://myAtlasDBUser:<password>@myatlasclusteredu.h09az9g.mongodb.net/'

client = MongoClient(MONGO_DB_URI)

for db in client.list_databases():
    print(db)

client.close()