import os
import openai
import pymongo

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_database():
   CONNECTION_STRING = "mongodb://root:root@mongo:27017/"
   client = pymongo.MongoClient(CONNECTION_STRING)
   print(client.list_database_names())
   
get_database()