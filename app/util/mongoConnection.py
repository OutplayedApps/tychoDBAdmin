from pymongo import MongoClient
from secret import DB_MONGO_CONN_STRING
from bson import ObjectId
import json

# MongoClient is initialized only once.
uri = DB_MONGO_CONN_STRING
mongoClient = MongoClient(uri)
print "=== initializing mongo client ==="

def convertToList(queryResults):
    results = []
    for i in queryResults:
        i["id"] = i.pop("_id")
        results.append(i)
    return results

def fixQuery(query):
    for k, v in query.items():
        if k != 'questionNum':
            try:
                v = int(v)
            except ValueError:
                pass  # it was a string, not an int.
        if v:
            query[k] = v
        else:
            query.pop(k, None)
    return query

class MongoConnection(object):
    def __init__(self):
        client = mongoClient
        self.db = client['tycho']

    def get_collection(self, name):
        self.collection = self.db[name]

class QuestionsCollection(MongoConnection):
    #vendorNum - string
    #packetNum - int
    #setNum - int
    #questionNum - string

    def __init__(self):
       super(QuestionsCollection, self).__init__()
       self.get_collection('questions')

    def getQuestionList(self, query = None, **kwargs):
        """Returns a list of questions sorted by json query.
        """
        
        if query is None:
            query = {}
        else:
            query = fixQuery(query)
        print str(query)
        results = self.collection.find(query).limit (100)
        return convertToList(results)
        #centerId = kwargs['center'].pk
        #queryResults = self.collection.find({"center": centerId}, {"name": 1} );

    
    def getQuestionById(self, id):
        """Gets question metadata by ID.
        """
        queryResults = self.collection.find_one({"_id": ObjectId(id)} );
        return queryResults