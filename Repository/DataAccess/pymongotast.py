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

    def search(self, query, pDBName='test', pCollectionName='students'):
        db = self.myclient[pDBName]
        collection = db[pCollectionName]
        d = collection.find_one()
        return d

db=DB()
print(db.search(''))
