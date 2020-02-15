from pymongo import MongoClient

myclient=MongoClient(host='114.32.122.25',port=27017,username='mongo_root',password='Password777!Here')
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
