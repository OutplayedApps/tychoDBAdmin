from pymongo import MongoClient
from bson import ObjectId
import json
from datetime import datetime
import os

try:
    from secret import DB_MONGO_CONN_STRING
except ImportError:
    DB_MONGO_CONN_STRING = os.environ.get('DB_MONGO_CONN_STRING', '')

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
        try:
            v = int(v)
        except ValueError:
            pass  # it was a string, not an int.
        if v and k in ["tossupQ", "tossupA", "bonusQ", "bonusA"]:
            # search for CONTAINING this string.
            query[k] = {"$regex" : v}
        elif v:
            query[k] = v
        else:
            query.pop(k, None)
    return query

def fixData(query):
    for k, v in query.items():
        try:
            v = int(v)
        except ValueError:
            pass  # it was a string, not an int.
        if v and k in ["tossupQ", "tossupA", "bonusQ", "bonusA"]:
            # search for CONTAINING this string.
            query[k] = {"$regex" : v}
        elif v:
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
        results = self.collection.find(query).limit(100)
        return convertToList(results)
    
    def getQuestionById(self, id):
        """Gets question metadata by ID.
        """
        queryResults = self.collection.find_one({"_id": ObjectId(id)} );
        return queryResults
    
    def updateQuestion(self, id, question):
        question.pop('id[$oid]', None)
        question['date_modified'] = datetime.now().isoformat()
        self.collection.update_one( {"_id": ObjectId(id)}, {"$set": question} )
        return id
    
    def addQuestion(self, question):
        question['date_created'] = datetime.now().isoformat()
        question['date_modified'] = question['date_created']
        result = self.collection.insert_one(question)
        
        return result.inserted_id
    
    def deleteQuestion(self, id):
        self.collection.delete_one({"_id": ObjectId(id) })