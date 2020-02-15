from pymongo import MongoClient


# DB封裝
class DB ():
    def __init__(self, pHost='114.32.122.25', pPort=27017, pUsername='mongo_root', pPassword='Password777!Here'):
        self.myclient = MongoClient(
            host=pHost, port=pPort, username=pUsername, password=pPassword)

    def Insert(self, data, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        result = collection.insert(data)
        return result

    def search(self, query, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        d = collection.find_one()
        return d

db=DB()
print(db.search(''))
