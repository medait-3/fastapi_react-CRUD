#import statements
from pymongo import MongoClient

#create BD connection
connection = MongoClient("mongodb+srv://med:med@cluster0.adrsb.mongodb.net/test?retryWrites=true&w=majority")
