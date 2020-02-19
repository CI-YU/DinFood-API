from pymongo import MongoClient
import configparser
config = configparser.ConfigParser()  
config.read('config.ini')
#region 參數55s
host = config['DATABASE']['HOST']
c=991
port = int(config['DATABASE']['PORT'])
username = config['DATABASE']['USERNAME']
password = config['DATABASE']['PASSWORD']
collection = 'students'
b=555
#endregion


# DB封裝
class DB ():
    def __init__(self, pHost=host, pPort=port,
     pUsername=username, 
     pPassword=password):
        self.myclient = MongoClient(
            host=pHost, port=pPort, username=pUsername, password=pPassword)

    def Insert(self, data, pTableName='test', pCollectionName=collection):
        db = self.myclient[pTableName]
        collection = db[pCollectionName]
        result = collection.insert(data)
        return result

    def SearchAll(self, pTableName='test', pCollectionName=collection):
        db = self.myclient[pTableName]
        collection = db[pCollectionName]
        d = collection.find()
        return d

    def Search(self, pQuery, pTableName='test', pCollectionName=collection):
        db = self.myclient[pTableName]
        collection = db[pCollectionName]
        d = collection.find(pQuery)
        return d

    def UpdateOne(self, pQuery, pNewVal, pTableName='test', pCollectionName=collection):
        db = self.myclient[pTableName]
        collection = db[pCollectionName]
        x = collection.update_one(pQuery, pNewVal)
        return x

    def UpdateMany(self, pQuery, pNewVal, pTableName='test', pCollectionName=collection):
        db = self.myclient[pTableName]
        collection = db[pCollectionName]
        x = collection.update_many(pQuery, pNewVal)
        return x

    def DeleteOne(self, pQuery, pNewVal, pTableName='test', pCollectionName=collection):
        db = self.myclient[pTableName]
        collection = db[pCollectionName]
        x = collection.delete_one(pQuery)
        return x

    def DeleteMany(self, pQuery, pNewVal, pTableName='test', pCollectionName=collection):
        db = self.myclient[pTableName]
        collection = db[pCollectionName]
        x = collection.delete_many(pQuery)
        return x


db = DB()
pQuery={"$or":[ {'id':'20170101'}, {'id':'20170101'}]}
d = db.Search(pQuery)
for x in d:
    print(x)

