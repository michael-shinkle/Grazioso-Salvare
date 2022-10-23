from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from bson.objectid import ObjectId
from pprint import pprint


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, userName, password, ip, port, db):
        USERNAME = userName
        PASSWORD = password
        IP = ip
        PORT = port
        DATABASE = db
        dbUrl = f'mongodb://{USERNAME}:{PASSWORD}@{IP}:{PORT}/{DATABASE}?authSource={DATABASE}'
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient(dbUrl, serverSelectionTimeoutMS=100)
        self.database = self.client[DATABASE]
        try:
            self.client.admin.command('ping')
            print(f'Successfully connected to database {DATABASE}')
        except ConnectionFailure as err:
            raise Exception(err)
        except OperationFailure as err:
            raise Exception(err)

    
    def create(self, data, collection):
        """
        Creates a new document in the mongo database
        
        :param data: dictionary with document to add data
        :param collection: string with the name of collection to use
        :return: true for succesful document creation, false for unsucessful document creation
        :raise Exception: if data dictionary is missing a field   
        """ 

        # list of keys required for each database document to maintain consistency
        keyList = list(self.database[collection].find_one({}, {'_id': False}).keys())
        
        # checks that new document has all required keys
        for key in keyList:
            if key not in data:
                raise Exception(f'Missing value for {key}')

        newDoc = self.database[collection].insert_one(data)
        # if newDoc has an inserted id then document was successfully created
        if newDoc.inserted_id:
            print(f'New document added to database, ID: {newDoc.inserted_id}')
            return True
        else:
            print('Unable to add document to database.')
            return False


    def readAll(self, query, collection):
        """
        Reads all documents matching query in the mongo database

        :param query: dictionary with query data
        :param collection: string with the name of collection to use
        :return: Cursor to location of document found in mongo
        """
        x = self.database[collection].find(query, {'_id':False})
        return x


    def readOne(self, query, collection):
        """
        Reads the first document matching query in the mongo database

        :param query: dictionary with query data
        :param collection: string with the name of collection to use
        :return: dictionary with all of the document data
        """
        x = self.database[collection].find_one(query)
        return x


    def updateOne(self, query, updateValue, collection):
        """
        Updates the first document matching query in the mongo database

        :param query: dictionary with query data
        :param updateValue: dictionary with key and value to update
        :param collection: string with the name of collection to use
        :return: updateResult Object
        """
        updateCommand = {'$set': updateValue}
        x  = self.database[collection].update_one(query, updateCommand)
        return x


    def updateMany(self, query, updateValue, collection):
        """
        Updates all documents matching query in the mongo database

        :param query: dictionary with query data
        :param updateValue: dictionary with key and value to update
        :param collection: string with the name of collection to use
        :return:updateResult Object
        """
        updateCommand = {'$set' : updateValue}
        x = self.database[collection].update_many(query, updateCommand)
        return x


    def deleteOne(self, query, collection):
        """
        Deletes first document matching query in the mongo database

        :param query: dictionary with query data
        :param collection: string with the name of collection to use
        :return: deleteResult Object
        """
        x = self.database[collection].delete_one(query)
        return x
        


    def deleteMany(self, query, collection):
        """
        Deletes first document matching query in the mongo database

        :param query: dictionary with query data
        :param collection: string with the name of collection to use
        :return: deletResult Object
        """
        x = self.database[collection].delete_many(query)
        return x

