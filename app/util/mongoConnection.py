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

class MongoConnection(object):
    def __init__(self):
        client = mongoClient
        self.db = client['tycho']

    def get_collection(self, name):
        self.collection = self.db[name]

class QuestionsCollection(MongoConnection):
    def __init__(self):
       super(QuestionsCollection, self).__init__()
       self.get_collection('questions')

    def getQuestionList(self, **kwargs):
        """Returns a list of questions
        """
        results = self.collection.find().limit (100)
        return convertToList(results)
        #centerId = kwargs['center'].pk
        #queryResults = self.collection.find({"center": centerId}, {"name": 1} );

    
    def getQuestionById(self, id):
        """Gets question metadata by ID.
        """
        queryResults = self.collection.find_one({"_id": ObjectId(id)} );
        return queryResults