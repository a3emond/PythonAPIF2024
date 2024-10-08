from database.__init__ import database
import app_config as config

def create_user(user):
    collection = database.database[config.CONST_USER_COLLECTION]
    return collection.insert_one(user.__dict__)