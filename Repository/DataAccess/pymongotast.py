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

    def Search(self, pQuery, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        d = collection.find(pQuery)
        return d

    def UpdateOne(self, pQuery, pNewVal, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        x = collection.update_one(pQuery, pNewVal)
        return x

    def UpdateMany(self, pQuery, pNewVal, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        x = collection.update_many(pQuery, pNewVal)
        return x

    def DeleteOne(self, pQuery, pNewVal, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        x = collection.delete_one(pQuery)
        return x

    def DeleteMany(self, pQuery, pNewVal, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        x = collection.delete_many(pQuery)
        return x


db = DB()
d = db.Search(pQuery={'id': '20170101'})
for x in d:
    print(x)
