from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:42769' % (username, password))
        self.database = self.client['AAC']

# create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# read_all method that returns cursor
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False})
        return cursor

# read method to implement the R in CRUD
    def read(self, data):
        return self.database.animals.find_one(data)

# update method to implement the U in CRUD
    def update(self, query, data):
        return self.database.animals.update_one(query, data) # two values are passed in, both should be dictionary
    
# delete method to implement the D in CRUD
    def delete(self, data):
        return self.database.animals.remove(data)  # data should be dictionary

