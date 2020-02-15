from pymongo import MongoClient
import configparser
config = configparser.ConfigParser()  
config.read('config.ini')
p = config['DATABASE']['PORT']
myclient=MongoClient(host=config['DATABASE']['HOST'],
port=int(p),username=config['DATABASE']['USERNAME'],password=config['DATABASE']['PASSWORD'])
db = myclient['test']
collection = db['students']
def insert():
    student = {
        'id': '20170101',
        'name': 'Jordan',
        'age': 20,
        'gender': 'male'
    }
    result = collection.insert(student)
    print(result)
def search():
    d= collection.find_one()
    print(d)
    
search()
