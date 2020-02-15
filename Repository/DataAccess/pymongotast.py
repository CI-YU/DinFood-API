from pymongo import MongoClient
import configparser
config = configparser.ConfigParser()  
config.read('config.ini')


# DB封裝
class DB ():
    def __init__(self, pHost=config['DATABASE']['HOST'], pPort=int(config['DATABASE']['PORT']),
     pUsername=config['DATABASE']['USERNAME'], 
     pPassword=config['DATABASE']['PASSWORD']):
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
