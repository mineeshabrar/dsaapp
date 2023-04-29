from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

connection_string = "mongodb+srv://mineeshabrar:mineeshabrar@e-curricular.sv9lmse.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string, server_api=ServerApi('1'))
db = client["dsa-app"]
