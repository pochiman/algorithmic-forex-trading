from pymongo import MongoClient, errors

from constants.defs import MONGO_CONN_STR

class DataDB:

    SAMPLE_COLL = "forex_sample"

    def __init__(self):
        self.client = MongoClient(MONGO_CONN_STR)
        self.db = self.client.forex_learning

    def test_connection(self):
        print(self.db.list_collection_names())

    def add_one(self, collection, ob):
        try:
            _ = self.db[collection].insert_one(ob)
        except errors.InvalidOperation as error:
            print("add_one error:", error)

    def add_many(self, collection, list_ob):
        try:
            _ = self.db[collection].insert_many(list_ob)
        except errors.InvalidOperation as error:
            print("add_many error:", error)
