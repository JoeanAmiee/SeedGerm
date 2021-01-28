from tinydb import TinyDB
from tinydb import Query

query = Query()
db = TinyDB('test.json')
db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})
print(db.all())
db.update({'count': 100}, query.type == 'apple')
print(db.all())
db.remove(query.type == 'peach')
print(db.all())
db.truncate()
print(db.all())
